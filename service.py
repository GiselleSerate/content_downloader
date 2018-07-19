from flask import Flask
from flask import abort
from flask import render_template
from flask import request
from flask import send_file
import os

from .content_downloader import ContentDownloader

app = Flask(__name__)
download_dir = '/tmp/content_downloader/cache'


@app.route('/')
def index():
    """
    Default route, return simple HTML page
    :return:  index.htnl template
    """
    return render_template('index.html', title='PanOS Content Update Utility')


@app.route('/download_content', methods=['POST'])
def download_content():
    posted_json = request.get_json(force=True)
    try:
        username = posted_json['username']
        password = posted_json['password']
        package = posted_json['package']
        update = posted_json.get('force_update', "True")

        print(update)
        print(type(update))

    except KeyError:
        abort(400, 'not all keys present')
        return

    package_dir = os.path.join(download_dir, package)
    print(package_dir)
    if not os.path.exists(package_dir):
        os.makedirs(package_dir)

    if str(update) == "False":
        # the user does not need the latest and greatest and just wants something relatively recent
        cached_files = os.listdir(package_dir)
        # do we have a previously downloaded file?
        if len(cached_files) > 0:
            # yep, just return here, if not, continue getting the latest update
            return send_file(os.path.join(package_dir, cached_files[0]))

    content_downloader = ContentDownloader(username=username, password=password, package=package,
                                           debug=True)

    # Check latest version. Login if necessary.
    token, updates = content_downloader.check()

    filename, foldername, latestversion = content_downloader.find_latest_update(updates)

    # check out cache dir
    downloaded_versions = list()
    for f in os.listdir(download_dir):
        downloaded_versions.append(f)

    # Check if already downloaded latest and do nothing
    if filename in downloaded_versions:
        return send_file(os.path.join(download_dir, filename))

    # Get download URL
    fileurl = content_downloader.get_download_link(token, filename, foldername)

    filename = content_downloader.download(download_dir, fileurl, filename)

    return send_file(os.path.join(download_dir, filename))


@app.before_first_request
def init_application():
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

