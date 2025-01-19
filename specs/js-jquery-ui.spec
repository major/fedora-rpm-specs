%global jsname jquery-ui

Name:		js-%{jsname}
Version:	1.14.1
Release:	2%{?dist}
Summary:	jQuery user interface

License:	MIT
URL:		https://jqueryui.com/
Source0:	https://github.com/jquery/%{jsname}/archive/%{version}/%{jsname}-%{version}.tar.gz
#		We need to bundle build dependencies since they are no
#		longer available in Fedora. This uses the same
#		technique as the js-jquery package.
Source1:	%{jsname}-%{version}-node-modules.tar.gz
#		Script to create the above sources
Source2:	create-source.sh

BuildArch:	noarch
BuildRequires:	nodejs >= 1:16
BuildRequires:	web-assets-devel
BuildRequires:	python3
BuildRequires:	python3-rcssmin
Requires:	js-jquery >= 1.12.0
Requires:	web-assets-filesystem

%description
A curated set of user interface interactions, effects, widgets, and
themes built on top of the jQuery JavaScript Library.

%prep
%setup -q -n %{jsname}-%{version} -a 1
rm -rf dist

%build
./node_modules/grunt-cli/bin/grunt -v requirejs:js concat:css uglify:main

# Provide a compressed version of the cascading style sheet
python3 -m rcssmin -b < dist/jquery-ui.css > dist/jquery-ui.min.css

%install
mkdir -p %{buildroot}%{_jsdir}/%{jsname}
install -m 644 -p dist/* %{buildroot}%{_jsdir}/%{jsname}
mkdir -p %{buildroot}%{_jsdir}/%{jsname}/images
install -m 644 -p themes/base/images/* %{buildroot}%{_jsdir}/%{jsname}/images

%files
%{_jsdir}/%{jsname}
%license LICENSE.txt
%doc AUTHORS.txt CONTRIBUTING.md README.md

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 13 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.14.1-1
- Update to version 1.14.1

* Mon Aug 12 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.14.0-1
- Update to version 1.14.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Apr 28 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.13.3-1
- Update to version 1.13.3

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 11 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.13.2-1
- Update to version 1.13.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.13.0-3
- Change CSS minifier from yuicompressor to rcssmin on Fedora

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 11 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.13.0-1
- Update to version 1.13.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Mar 27 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.12.1-2
- Provide a compressed version of the cascading style sheet

* Sat Feb 27 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.12.1-1
- First packaging for Fedora
