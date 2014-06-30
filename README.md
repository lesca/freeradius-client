To Use Packaged RPM
======================
- wget --no-check-certificate https://github.com/lesca/freeradius-client/raw/master/freeradius-client-1.1.6-0.x86_64.rpm

To Build RPM
======================

Install packages
----------------------
- yum install rpm-build redhat-rpm-config
- yum groupinstall "Development tools"

Create Environment Folders
----------------------
- mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

Create rpmmacros 
----------------------
- vim ~/.rpmmacros
- %_topdir %(echo $HOME)/rpmbuild
- %_tmppath %(echo $HOME)/rpmbuild/tmp

Download source
----------------------
- cd ~/rpmbuild/SOURCES
- wget -c ftp://ftp.freeradius.org/pub/freeradius/freeradius-client-1.1.6.tar.gz

To build rpm package for freeradius-client
----------------------
- rpmbuild -ba ~/rpmbuild/SPECS/freeradius-client.spec
