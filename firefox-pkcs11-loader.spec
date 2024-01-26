# needed to avoid error
# File /builddir/build/BUILD/firefox-pkcs11-loader-3.13.0/debugsourcefiles.list empty in section %file
%global debug_package %{nil}

# in %%cmake section, check if the comment still applies on versions > 3.13.0

Name:           firefox-pkcs11-loader
Version:        3.13.6
Release:        12%{?dist}
Summary:        Helper script for Firefox that sets up the browser for authentication with Estonian ID-card
License:        LGPLv2+
URL:            https://github.com/open-eid/firefox-pkcs11-loader
Source:         %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%if 0%{?el7}
BuildRequires: cmake3
%else
BuildRequires: cmake
%endif
BuildRequires: make
Requires:       opensc%{?_isa}
Requires:       pcsc-lite%{?_isa}
Requires:       pcsc-lite-ccid%{?_isa}

# mozilla-filesystem is required to install files into
# %%{_libdir}/mozilla and
# %%{_datadir}/mozilla/extensions/
# Comment author: Germano Massullo
Requires:       mozilla-filesystem
# old name was  firefox-esteidpkcs11loader
Obsoletes:      firefox-esteidpkcs11loader <= 3.12.0-2
Provides:       firefox-esteidpkcs11loader = %{version}-%{release}

%description
This package provides a helper script for Firefox that sets up the browser for
authentication with Estonian ID-card.

%prep
%setup -q -n %{name}-%{version}
# -DCMAKE_INSTALL_LIBDIR:PATH=%%{_libdir} is needed to avoid
# https://github.com/open-eid/firefox-pkcs11-loader/issues/10
# and to avoid that the build system will try installing files
# under hardcoded /usr/lib/... instead of %{_libdir}
# Comment author: Germano Massullo
%if 0%{?el7}
%{cmake3} . -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir}
%endif
%if ((0%{?el} > 8) || (0%{?fedora} > 32))
%{cmake} -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir}
%endif
%if ((0%{?fedora} <= 32) || (0%{?el8}))
%{cmake} . -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir}
%endif

%build
# concerning following cp command
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/S7AQI5UPBJXOPWIDPDGW2NIOSR2YGWFY/
%if ((0%{?el} > 8) || (0%{?fedora} > 32))
 cp -a *.xpi %{_vpath_builddir}/
%endif
# onepinopenscpkcs11.json contains line
# "path": "onepin-opensc-pkcs11.so",
# that tells Firefox what is the library it has to load. Since in Fedora
# onepin-opensc-pkcs11.so is not defined in LD path, so Firefox cannot load it
# by simply knowing its name, a complete path must be used.
# Therefore the replacement is done with sed.
# Nikos Mavrogiannopoulos (opensc co-maintainer) said that
# PKCS#11 modules in Fedora are not in LD path. The reason is that they are not
# generic libraries, but rather loadable modules. Their location is
# "%%{_libdir}/pkcs11"
# Concerning the sed command, I had to use
# sed -i 's/onepin-opensc-pkcs11.so/\%_prefix\/%{_lib}\/pkcs11\/onepin-opensc-pkcs11.so/' onepinopenscpkcs11.json
# instead of
# sed -i 's/onepin-opensc-pkcs11.so/%{_libdir}\/pkcs11\/onepin-opensc-pkcs11.so/' onepinopenscpkcs11.json
# because %%{_libdir} will insert /usr/lib64 and I don't know how to escape the / in the middle.
# Note: 
# %%_prefix is a macro for /usr directory
# %%{_lib} is a macro for /lib (or /lib64 on 64 bit architectures) directory
# Comment author: Germano Massullo
sed -i 's/onepin-opensc-pkcs11.so/\%_prefix\/%{_lib}\/pkcs11\/onepin-opensc-pkcs11.so/' onepinopenscpkcs11.json
%if ((0%{?el} > 8) || (0%{?fedora} > 32))
%cmake_build
%else
make %{?_smp_mflags}
%endif

%install
%if ((0%{?el} > 8) || (0%{?fedora} > 32))
%cmake_install
%else
make install DESTDIR=%{buildroot}
%endif

%files
%doc README.md AUTHORS RELEASE-NOTES.md
%license LICENSE.LGPL
# %%{_datadir} is a macro for /usr/share
%{_datadir}/mozilla/extensions/*
# %% dir creates a directory under a specific path
# and "marks" the package as directory owner
%dir %{_libdir}/mozilla/pkcs11-modules/
%{_libdir}/mozilla/pkcs11-modules/onepinopenscpkcs11.json
%{_libdir}/mozilla/pkcs11-modules/idemiaawppkcs11.json

%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jan 30 2021 Germano Massullo <germano.massullo@gmail.com> - 3.13.6-5
- Applied CMake to do out-of-source builds change

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.6-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Dmitri Smirnov <dmitri@smirnov.ee> - 3.13.6-1
- Upstream release 3.13.6

* Mon Apr 06 2020 Dmitri Smirnov <dmitri@smirnov.ee> 3.13.5-1
- Upstream release 3.13.5: Create linux policy to install Firefox extension from Mozilla Addon store

* Fri Jan 31 2020 Dmitri Smirnov <dmitri@smirnov.ee> 3.13.4-1
- Upstream release 3.13.4: Distribute Mozilla AMO signed extensions

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Dmitri Smirnov <dmitri@smirnov.ee> 3.13.3-1
- Upstream release 3.13.3: Unload old IDEMIA PKCS11

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Dmitri Smirnov <dmitri@smirnov.ee> 3.13.1-1
- upstream release 3.13.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 29 2018 Germano Massullo <germano.massullo@gmail.com> - 3.13.0-7
- removed Requires: esteidcerts

* Thu Mar 22 2018 Germano Massullo <germano.massullo@gmail.com> - 3.13.0-6
- added macros for cmake3 on EPEL7

* Wed Mar 07 2018 Germano Massullo <germano.massullo@gmail.com> - 3.13.0-5
- removed BuildArch: noarch
- %%files section: replaced again %_prefix/lib with %%{_libdir} because the package is not a noarch package
- added %%global debug_package %%{nil} (see comments)
- readded cmake flag -DCMAKE_INSTALL_LIBDIR:PATH=%%{_libdir} (see comments)

* Tue Mar 06 2018 Germano Massullo <germano.massullo@gmail.com> - 3.13.0-4
- %%files section: replaced again %%{_libdir} with %_prefix/lib because noarch packages files should only go into /usr/lib
- removed cmake flag -DCMAKE_INSTALL_LIBDIR:PATH=%%{_libdir} because noarch packages files should only go into /usr/lib

* Tue Mar 06 2018 Germano Massullo <germano.massullo@gmail.com> - 3.13.0-3
- added sed command to add full onepin-opensc-pkcs11.so path to onepinopenscpkcs11.json (see comments)
- added -DCMAKE_INSTALL_LIBDIR:PATH=%%{_libdir} flag (see comments)
- replaced %%_prefix/lib with %%{_libdir}

* Sun Mar 04 2018 Germano Massullo <germano.massullo@gmail.com> - 3.13.0-2
- improved Obsoletes and Provides
- replaced with macros the hardcoded library path for JSON file

* Thu Feb 22 2018 Germano Massullo <germano.massullo@gmail.com> - 3.13.0-1
- 3.13.0 release
- added Obsoletes: firefox-esteidpkcs11loader
- added %%license section
- added %%dir %%{_prefix}/lib/mozilla/pkcs11-modules/
- added %%_prefix/lib/mozilla/pkcs11-modules/onepinopenscpkcs11.json

* Wed Jun 15 2016 Mihkel Vain <mihkel@fedoraproject.org> - 3.12.0-1
- New upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jul 11 2015 Mihkel Vain <mihkel@fedoraproject.org> - 3.11.0-1
- New upstream release
- Spec file cleanups

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.0.1052-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 10 2015 Mihkel Vain <mihkel@fedoraproject.org> - 3.8.0.1052-5
- Project moved to github
- Require pcsc-lite-ccid (#1210639)

* Wed Nov 12 2014 Mihkel Vain <mihkel@fedoraproject.org> - 3.8.0.1052-4
- Use onepin module patch with opensc 0.14

* Sun Jun 22 2014 Mihkel Vain <mihkel@fedoraproject.org> - 3.8.0.1052-3
- Rename package to firefox-esteidpkcs11loader and obsolete mozilla-esteid

* Fri Jun 20 2014 Mihkel Vain <mihkel@fedoraproject.org> - 3.8.0.1052-2
- Fix spec file according to suggestions

* Fri Jan 17 2014 Mihkel Vain <turakas@gmail.com> - 3.8.0.1052-1
- First rpm package for Fedora

* Fri Aug 13 2010 RIA <info@ria.ee> 1.0-1
- first build no changes
