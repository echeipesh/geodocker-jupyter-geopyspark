%define _topdir   /tmp/rpmbuild
%define name      gdal213
%define release   33
%define version   2.1.3

BuildRoot: %{buildroot}
Summary:   GDAL
License:   X/MIT
Name:      %{name}
Version:   %{version}
Release:   %{release}
Source:    gdal-%{version}.tar.gz
Prefix:    /usr/local
Group:     Geography

%description
GDAL

%prep
%setup -q -n gdal-2.1.3

%build
LDFLAGS='-L/usr/local/lib -L/usr/local/lib64' ./configure --prefix=/usr/local
make -k -j 33 || make

%install
make DESTDIR=%{buildroot} install

%package lib
Group: Geography
Summary: GDAL
%description lib
The libraries

%files lib
%defattr(-,root,root)
/usr/local/lib/*

%files
%defattr(-,root,root)
/usr/local/*