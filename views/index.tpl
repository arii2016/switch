<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - Camera Edit</title>
    <link rel="stylesheet" type="text/css" href="/static/content/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/site.css" />
    <script src="/static/scripts/modernizr-2.6.2.js"></script>
</head>

<body>
    <div class="container body-content">
        <h2>{{ title }}</h2>
        <hr />
        <div class="row">
            <div class="col-md-3 col-sm-6">
                <a class="btn btn-primary btn-lg" href="javascript:;" onclick="fnOn(); return false;">ON</a>
            </div>
            <div class="col-md-3 col-sm-6">
                <a class="btn btn-primary btn-lg" href="javascript:;" onclick="fnOff(); return false;">OFF</a>
            </div>
        </div>
        <hr />
        <footer>
        </footer>
    </div>

    <script src="/static/scripts/jquery-1.10.2.js"></script>
    <script src="/static/scripts/bootstrap.js"></script>
    <script src="/static/scripts/respond.js"></script>
    <script src="/static/scripts/site.js?ver=1.00"></script>
</body>
</html>
