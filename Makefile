PREFIX?=/etc/X11/
PROJECT_NAME=synconf
BASEDIR=$(PREFIX)/xorg.conf.d/

VERSION=0.0.1


COMMONSRC=

.PHONY: depend clean

default: install

init:
	install -m755 -d $(BASEDIR)

copy:
	cp -Rv src/xorg.conf.d/* $(BASEDIR)

install: init copy

rpm-clean:
	rm -f ${HOME}/rpmbuild/SOURCES/*

rpm-prep: rpm-clean
	mkdir -p ${HOME}/rpmbuild/SOURCES/
	tar --transform="s/\./${PROJECT_NAME}-${VERSION}/" -cf ${HOME}/rpmbuild/SOURCES/${PROJECT_NAME}-${VERSION}.tar.gz ./ --gzip

rpm: rpm-prep
	rpmbuild -ba dist/$(PROJECT_NAME).spec
