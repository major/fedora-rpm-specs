Summary: Visualization and Computer Graphics Library
Name: vcglib
Version: 1.0.1
Release: 7%{?dist}
License: GPLv2+ and GPLv3+
URL: http://vcg.isti.cnr.it/vcglib/
Source: https://github.com/cnr-isti-vclab/vcglib/archive/v%{version}.tar.gz
BuildRequires: sed
Requires: /usr/bin/pkg-config
Requires: eigen3 glibc-headers
%description
The Visualization and Computer Graphics Library (VCG for short) is a 
open source portable C++ templated library for manipulation, processing 
and displaying with OpenGL of triangle and tetrahedral meshes.

%package devel
Summary: Include files for vcglib
License: GPLv2+ and GPLv3+
Provides: vcglib-static = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Include files for vcglib

%global debug_package %{nil} 
%prep
%setup -q

%build
find vcg img -name '*.cpp' | xargs -r rm
find . -name '*.h' -exec chmod a-x '{}' ';'

%install 
mkdir -p %{buildroot}%{_includedir}/%{name}/wrap
cp -r vcg img %{buildroot}%{_includedir}/%{name}

cp -a wrap/*.h wrap/{gcache,gl,glw,igl,io_edgemesh,io_tetramesh,io_trimesh,math,minpack,mt,opensg,system} \
    %{buildroot}%{_includedir}/%{name}/wrap
rm %{buildroot}%{_includedir}/%{name}/wrap/system/{getopt,qgetopt}.*

mkdir -p %{buildroot}%{_docdir}/%{name}
install -m 644 README.md %{buildroot}%{_docdir}/%{name} 

mkdir -p %{buildroot}%{_datarootdir}/pkgconfig
cat > %{buildroot}%{_datarootdir}/pkgconfig/vcglib.pc << EOT
prefix=/usr
exec_prefix=${prefix}

Name: vcglib
Description: Visualization and Computer Graphics Library 
Requires: eigen3
Version: 1.0.1
Libs:
Cflags: -I/usr/include/%{name}
EOT

%files
%license LICENSE.txt
%doc README.md

%files devel
%{_includedir}/%{name}
%{_datarootdir}/pkgconfig/vcglib.pc

%changelog 
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Apr 10 2019 J. Scheurich <mufti11@web.de> - 1.0.1
- initial RPM packaging


