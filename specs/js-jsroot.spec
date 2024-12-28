%global jsname jsroot

Name:		js-%{jsname}
Version:	7.8.0
Release:	1%{?dist}
Summary:	JavaScript ROOT - Interactive numerical data analysis graphics

#		Most files are MIT, d3.mjs is BSD, dat.gui.mjs is Apache-2.0
License:	MIT AND BSD-3-Clause AND Apache-2.0
URL:		https://jsroot.gsi.de/
Source0:	https://github.com/root-project/%{jsname}/archive/%{version}/%{jsname}-%{version}.tar.gz
#		Use locally installed mathjax instead of remote installation.
Patch0:		%{name}-mathjax.patch

BuildArch:	noarch
BuildRequires:	web-assets-devel
Requires:	web-assets-filesystem
Requires:	mathjax3

%description
JavaScript ROOT provides interactive ROOT-like graphics in web browsers.
Data can be read and displayed from binary and JSON ROOT files.

%prep
%setup -q -n %{jsname}-%{version}
%patch -P0 -p1

%build
# nothing to do

%install
mkdir -p %{buildroot}%{_jsdir}/%{jsname}

# In upstream's released version modules/d3.mjs and modules/three.mjs
# are minified, but in root's bundled version they ar not.
# Leave them unminified in Fedora.
for d in modules modules/base modules/draw modules/geom modules/gpad \
    modules/gui modules/hist modules/hist2d ; do
mkdir %{buildroot}%{_jsdir}/%{jsname}/${d}
install -m 644 -p ${d}/*.mjs %{buildroot}%{_jsdir}/%{jsname}/${d}
done

ln -rs %{buildroot}%{_jsdir}/mathjax@3 %{buildroot}%{_jsdir}/%{jsname}/mathjax

mkdir %{buildroot}%{_jsdir}/%{jsname}/build
install -m 644 -p build/jsroot.js %{buildroot}%{_jsdir}/%{jsname}/build

mkdir %{buildroot}%{_jsdir}/%{jsname}/scripts
install -m 644 -p scripts/*.js %{buildroot}%{_jsdir}/%{jsname}/scripts

# Upstream's released version adds a copy with the ending .min.js
# Despite its name it is not minified. Do the same for Fedora.
ln %{buildroot}%{_jsdir}/%{jsname}/scripts/JSRoot.core.js \
   %{buildroot}%{_jsdir}/%{jsname}/scripts/JSRoot.core.min.js

mkdir -p %{buildroot}%{_jsdir}/%{jsname}/files
install -m 644 -p files/* %{buildroot}%{_jsdir}/%{jsname}/files

mkdir -p %{buildroot}%{_jsdir}/%{jsname}/img
install -m 644 -p img/* %{buildroot}%{_jsdir}/%{jsname}/img

mkdir -p %{buildroot}%{_pkgdocdir}
ln -rs %{buildroot}%{_jsdir}/%{jsname}/build %{buildroot}%{_pkgdocdir}
ln -rs %{buildroot}%{_jsdir}/%{jsname}/img %{buildroot}%{_pkgdocdir}
ln -rs %{buildroot}%{_jsdir}/%{jsname}/modules %{buildroot}%{_pkgdocdir}
ln -rs %{buildroot}%{_jsdir}/%{jsname}/scripts %{buildroot}%{_pkgdocdir}

%pretrans -p <lua>
-- Remove links created by broken scriptlet in root-net-http
linkstoremove = {
  "%{_jsdir}/%{jsname}/img/img",
  "%{_jsdir}/%{jsname}/libs/libs",
  "%{_jsdir}/%{jsname}/scripts/scripts",
  "%{_jsdir}/%{jsname}/style/style"
}
for _, path in ipairs(linkstoremove) do
  st = posix.stat(path)
  if st and st.type == "link" then
    os.remove(path)
  end
end

%files
%{_jsdir}/%{jsname}
%license LICENSE libs/*.LICENSE
%doc %{_pkgdocdir}/*
%doc changes.md demo docs/* index.htm readme.md

%changelog
* Thu Dec 26 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 7.8.0-1
- Update to version 7.8.0

* Fri Nov 15 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 7.7.5-1
- Update to version 7.7.5

* Mon Aug 19 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 7.7.2-1
- Update to version 7.7.2

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 7.7.1-1
- Update to version 7.7.1
- Add backport patch to match root 6.32.02

* Sun Jun 09 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 7.7.0-1
- Update to version 7.7.0

* Sat Apr 06 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 7.5.5-1
- Update to version 7.5.5

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Nov 24 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 7.5.3-1
- Update to version 7.5.3

* Sat Oct 14 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 7.3.4-1
- Update to version 7.3.4

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 28 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 7.3.1-1
- Update to version 7.3.1

* Wed Mar 15 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 7.3.0-1
- Update to version 7.3.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.3.4-3
- Change CSS minifier from yuicompressor to rcssmin on Fedora

* Wed Jun 15 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.3.4-2
- Update backport patch to match root 6.26.04

* Tue Apr 05 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.3.4-1
- Update to version 6.3.4

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 05 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.2.1-1
- Update to version 6.2.1

* Mon Aug 16 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.2.0-1
- Update to version 6.2.0
- This version uses a newer javascript version syntax that requires a
  newer uglify-js version

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 11 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.9.1-1
- Update to version 5.9.1
- Change Requires to new js-jquery-ui package (also for EPEL 8)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 26 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.8.0-5
- Compatibility with uglifyjs v3 (no --preamble option)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.8.0-3
- Do not use closure-compiler for Fedora 33+ - it is orphaned and
  uninstallable with broken deps.

* Wed Jul 15 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.8.0-2
- No longer bundle js-jquery, js-jquery-mousewheel and
  js-jquery-ui-touch-punch for EPEL 8.
- Still bundle js-jquery-ui which is not available in EPEL 8.

* Mon Mar 23 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.8.0-1
- Update to version 5.8.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 23 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.7.2-1
- Update to version 5.7.2
- Bundle jquery and its dependants in EPEL 8 - not available

* Wed Aug 14 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.7.1-1
- Update to version 5.7.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.7.0-1
- Update to version 5.7.0

* Fri Mar 22 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.6.4-1
- Update to version 5.6.4

* Fri Feb 01 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.6.3-1
- Update to version 5.6.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 10 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.6.1-1
- Update to version 5.6.1

* Mon Nov 05 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.6.0-1
- Update to version 5.6.0

* Thu Aug 30 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.5.1-1
- Update to version 5.5.1

* Fri Jul 20 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.5.0-1
- Update to version 5.5.0
- Change dependency to js-jquery since js-jquery2 is orphaned

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.4.2-2
- Adapt symlinks to updated jquery-ui package

* Wed May 30 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.4.2-1
- Update to version 5.4.2

* Wed Apr 11 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.4.1-1
- Update to version 5.4.1

* Sat Feb 24 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.4.0-1
- Update to version 5.4.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.3.5-1
- Update to version 5.3.5

* Wed Jan 03 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.3.4-2
- Make Summary more informative
- Add files directory needed by root-net-http

* Mon Dec 25 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.3.4-1
- Initial packaging for Fedora
