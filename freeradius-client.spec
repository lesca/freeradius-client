Summary:        FreeRADIUS Client Software
Name:           freeradius-client
Version:        1.1.6
Release:        0
Obsoletes:      radiusc radiusclient radiusclient-ng
Group:          Productivity/Networking/Radius/Clients
License:        BSD
Packager:       Lesca Fang
URL:            http://www.freeradius.org/
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Prefix:         %{_prefix}

%description
A portable, easy-to-use and standard compliant library suitable for developing free and commercial software that need support for a RADIUS protocol (RFCs 2128 and 2139).

%prep
%setup -q
./configure

%build
make

%install
make "DESTDIR=$RPM_BUILD_ROOT" install

%files
%defattr(-, root, root)
/usr/local/

%changelog
* Sun Jun 29 2014 Lesca Fang
- Create this spec file for CentOS 6
