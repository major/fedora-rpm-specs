%global	githash	79ff51e50bacdf9516e0fa6eda278052c82f8ea5
%global	shorthash	%(c=%{githash}; echo ${c:0:7})
%global	gitdate	Mon, 13 Jul 2015 22:29:10 +0530
%global	tardate	20150713

%global	usegitsource	0

%global	mainver	0.12.6
#%%global	minorver	D%{?tardate}git%{shorthash}
#%%global	prerelease	1

%global	baserelease	6

Name:		wkhtmltopdf
Version:	%{mainver}
Release:	%{?prerelease:0.}%{baserelease}%{?minorver:.%minorver}%{?dist}
Summary:	Simple shell utility to convert html to pdf

# overall	LGPL-3.0-or-later
# docs/js/foundation.min.js and some other *.js		MIT
# docs/js/vendor/modernizr.js	says "MIT and BSD",  choose "MIT" for now
# docs/libwkhtmltox/jquery.js	MIT OR GPL-2.0-only
#
# SPDX confirmed
License:	LGPL-3.0-or-later
URL:		http://wkhtmltopdf.org/
#Source0:	https://github.com/%{name}/%{name}/archive/%{githash}/%{name}-%{mainver}-D%{tardate}git%{shorthash}.tar.gz
Source0:	https://github.com/%{name}/%{name}/archive/%{mainver}/%{name}-%{mainver}.tar.gz

BuildRequires:	make
BuildRequires:	qt5-qtwebkit-devel
BuildRequires:	qt5-qtxmlpatterns-devel
BuildRequires:	qt5-qtsvg-devel

%description
Simple shell utility to convert html to pdf using the webkit
rendering engine, and qt. 

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?isa} = %{version}-%{release}
Requires:	qtwebkit-devel%{?isa}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	doc
Summary:	Documentation for %{name}
License:	LGPL-3.0-or-later AND MIT AND (MIT OR GPL-2.0-only)
Requires:	%{name} = %{version}
BuildArch:	noarch

%description	doc
This package contains documentation for %{name}.

%prep
%if 0%{?usegitsource} >= 1
%setup -q -c -T -a 0
cd %{name}-*/
%else
%setup -q -n %{name}-%{mainver}%{?minorver:_%minorver}
%endif
# libdir handling.. better handling needed
sed -i.lib -e \
	'/INSTALLBASE/s|lib|%{_lib}|' \
	src/lib/lib.pro

# Remove BOM
sed -i.bom -e 's|\xEF\xBB\xBF||' AUTHORS
touch -r AUTHORS{.bom,}
rm -f AUTHORS.bom

%build
%if 0%{?usegitsource} >= 1
cd %{name}-*/
%endif
%{qmake_qt5}
make %{_smp_mflags}

%install
%if 0%{?usegitsource} >= 1
cd %{name}-*/
cp -a [A-Z]* examples/ docs/ ..
%endif

make install \
	INSTALL_ROOT=%{buildroot}%{_prefix}

%ldconfig_scriptlets


%files
%doc	AUTHORS
%license	LICENSE
%doc	CHANGELOG.md
%doc	CHANGELOG-OLD
%doc	README.md

%{_libdir}/libwkhtmltox.so.0*
%{_bindir}/wkhtmltoimage
%{_bindir}/wkhtmltopdf

%{_mandir}/man1/wkhtmltoimage.1*
%{_mandir}/man1/wkhtmltopdf.1*

%files devel
%doc    examples/
%{_libdir}/libwkhtmltox.so
%{_includedir}/wkhtmltox/

%files doc
%doc	docs/


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Mar 19 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.12.6-4
- SPDX migration

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.6-3.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.6-2.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.6-1.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.6-1.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.6-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.6-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.6-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug  9 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.12.6-1
- 0.12.6

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.5-1.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.5-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.5-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.5-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.12.5-1
- 0.12.5

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 20 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.12.4-1
- 0.12.4

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-2.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-2.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.12.3-2
- use %%qmake_qt5/%%qmake_qt4 macros to ensure proper build flags

* Tue Jan 26 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.12.3-1
- 0.12.3
- F-24: use qt5 qtwebkit

* Sun Aug  9 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.12.3-0.1.D20150713git79ff51e
- Update to 0.12.3 test release

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.2.1-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.12.2.1-1.1
- Rebuilt for GCC 5 C++11 ABI change

* Wed Jan 21 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.12.2.1-1
- 0.12.2.1

* Sat Jan 10 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.12.2-1
- 0.12.2

* Wed Jan  7 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.12.2-0.2.rc.71e97c1
- 0.12.2 rc-71e97c1

* Wed Nov 26 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.12.2-0.1.dev5dea253
- Update to the latest git

* Wed Aug 27 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.12.1-1
- 0.12.1

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun  3 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.12.0-1
- 0.12.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-0.2.rc1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 12 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.11.0-0.2.rc1
- Include examples/ directory to devel documents

* Mon Feb 11 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.11.0-0.1.rc1
- Initial packaging
