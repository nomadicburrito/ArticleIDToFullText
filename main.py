import requestSciDir, sys

sciDir=requestSciDir.requestSciDir(sys.argv[1], sys.argv[2])

sciDir.request()
sciDir.write()

print sciDir.r.status_code
