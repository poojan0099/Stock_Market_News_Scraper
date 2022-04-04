from paths import rootPath, cachePath, recentPath
import json
from equitybulls import getWithTimeout
import time
import os


def recentFileUpdater():
    try:
        with open(recentPath, 'w+') as f:
            recent = {
                "timestamp": time.time()
            }
            f.write(
                json.dumps(recent)
            )
    except Exception:
        return False
    return True


def fetcher(url, mode):
    heading_links = getWithTimeout(url=url, timeout=60)
    if(isinstance(heading_links, dict)):
        with open(cachePath, 'w+') as f:
            print("writing to temp.json", mode)
            f.write(
                json.dumps(heading_links)
            )
        recentFileUpdater()
    else:
        print(heading_links)
    return heading_links


def runwithCache(url="https://example.com", cache_time=30):
    # check if recent file exists
    if os.path.exists(recentPath):
        with open(recentPath, 'r') as f:
            recent = json.load(f)

            # 300 -> 5 minutes
            if time.time() - int(recent['timestamp']) > cache_time:
                print("recent file expired")
                return fetcher(url=url, mode='ran after expire')
            else:
                print("recent file exists but not expired")

                # check if the file exists
                if(os.path.exists(cachePath)):
                    print("cache file exists")
                    with open(cachePath, 'r') as f:
                        heading_links = json.load(f)
                        print("loading from cache file")
                        return heading_links
                else:
                    return fetcher(url=url, mode='ran new')
    else:
        recentFileUpdater()


if __name__ == '__main__':
    equitybullURL = "https://www.equitybulls.com/"
    runwithCache(url=equitybullURL, cache_time=300)