%global pkg  anthy-unicode
%bcond_without autoreconf

%if (0%{?fedora} > 35 || 0%{?rhel} > 7)
%bcond_with    xemacs
%else
%bcond_without xemacs
%endif


Name:  anthy-unicode
Version: 1.0.0.20211224
Release: 10%{?dist}
# The entire source code is LGPLv2+ and dictionaries is GPLv2. the corpus data is under Public Domain.
License: LGPL-2.0-or-later and GPL-2.0-or-later and LicenseRef-Fedora-Public-Domain
URL:  https://github.com/fujiwarat/anthy-unicode/wiki
BuildRequires: emacs
BuildRequires: gcc
BuildRequires: git
%if %{with xemacs}
BuildRequires: xemacs
# overlay.el is required by anthy-unicode.el and anthy-unicode-isearch.el
BuildRequires: xemacs-packages-extra
%endif
%if %{with autoreconf}
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: make
%endif

Source0: https://github.com/fujiwarat/anthy-unicode/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1: %{name}-init.el
# Upstreamed patches
#Patch0: %%{name}-HEAD.patch
Patch0: %{name}-HEAD.patch

Summary: Japanese character set input library for Unicode

%description
Anthy Unicode is another Anthy project and provides the library to input
Japanese on the applications, such as X applications and emacs. and the
user dictionaries and the users information which is used for the conversion,
is stored into their own home directory. So Anthy Unicode is secure than
other conversion server.

%package -n emacs-%{pkg}
Summary: Emacs files for %{pkg}
Requires: %{name} = %{version}-%{release}
Requires: emacs(bin) >= %{_emacs_version}
BuildArch: noarch

%description -n emacs-%{pkg}
This package contains the byte compiled elips packages to run %{pkg}
with GNU Emacs.

%if %{with xemacs}
%package -n xemacs-%{pkg}
Summary: XEmacs files for %{pkg}
Requires: %{name} = %{version}-%{release}
Requires: xemacs(bin) >= %{_xemacs_version}
BuildArch: noarch

%description -n xemacs-%{pkg}
This package contains the elips packages to run %{pkg} with GNU XEmacs.
%endif

%package devel
Summary: Header files and library for developing programs which uses Anthy Unicode
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
The anthy-devel package contains the development files which is needed to build
the programs which uses Anthy Unicode.


%prep
%autosetup -S git

%build
%if %{with autoreconf}
autoreconf -f -i -v
%endif
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# remove unnecessary files
rm $RPM_BUILD_ROOT%{_libdir}/lib*.la

## for emacs-anthy
mkdir -p $RPM_BUILD_ROOT%{_emacs_sitestartdir}
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}

%if %{with xemacs}
## for xemacs-anthy
mkdir -p $RPM_BUILD_ROOT%{_xemacs_sitestartdir}
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_xemacs_sitestartdir}
# FIXME lisp build
pushd $RPM_BUILD_DIR/%{name}-%{version}/src-util
make clean
#make EMACS=xemacs lispdir="%%{_xemacs_sitelispdir}/%%{pkg}"
# The latest /usr/share/automake-*/am/lisp.am calls -L option for
# $(EMACS) --batch but -L is not supported by xemacs.
# Copy elisp-comp script here from old automake
xemacs --batch --eval '(setq load-path (cons nil load-path))' -f batch-byte-compile *.el
make
make install-lispLISP DESTDIR=$RPM_BUILD_ROOT EMACS=xemacs lispdir="%{_xemacs_sitelispdir}/%{pkg}" INSTALL="install -p"
popd
%endif

%check
sed -e "s|@datadir@|$PWD|" -e "s|@PACKAGE@|mkanthydic|" \
  anthy-unicode.conf.in > test.conf
_TEST_ENV="LD_LIBRARY_PATH=$PWD/src-main/.libs:$PWD/src-worddic/.libs"
_TEST_ENV="$_TEST_ENV CONFFILE=$PWD/test.conf"
cd test
env $_TEST_ENV ./anthy --all
env $_TEST_ENV ./checklib
cd ../src-util
env $_TEST_ENV ./anthy-dic-tool-unicode --load dic-tool-input
diff $HOME/.config/anthy/private_words_default dic-tool-result
env $_TEST_ENV ./anthy-dic-tool-unicode --dump
mkdir -p $HOME/.anthy
mv $HOME/.config/anthy/private_words_default $HOME/.anthy
env $_TEST_ENV ./anthy-dic-tool-unicode --migrate
diff $HOME/.config/anthy/private_words_default dic-tool-result
cd ..


%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog DIARY NEWS README
%license COPYING
%{_bindir}/*
# If new keywords are added in conf files, "noreplace" flag needs to be deleted
%config(noreplace) %{_sysconfdir}/*.conf
%{_libdir}/lib*.so.*
%{_datadir}/%{pkg}/

%files -n emacs-%{pkg}
%doc doc/ELISP
%{_emacs_sitelispdir}/%{pkg}/*.el
%{_emacs_sitelispdir}/%{pkg}/*.elc
%{_emacs_sitestartdir}/*.el
%dir %{_emacs_sitelispdir}/%{pkg}

%if %{with xemacs}
%files -n xemacs-%{pkg}
%doc doc/ELISP
%{_xemacs_sitelispdir}/%{pkg}/*.el
%if %{with xemacs}
%{_xemacs_sitelispdir}/%{pkg}/*.elc
%endif
%{_xemacs_sitestartdir}/*.el
%dir %{_xemacs_sitelispdir}/%{pkg}
%endif

%files devel
%doc doc/DICLIB doc/DICUTIL doc/GLOSSARY doc/GRAMMAR doc/GUIDE.english doc/ILIB doc/LEARNING doc/LIB doc/MISC doc/POS doc/SPLITTER doc/TESTING doc/protocol.txt
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.20211224-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.20211224-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Takao Fujiwara <fujiwara@redhat.com> 1.0.0.20211224-8
- Migrate license tag to SPDX

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.20211224-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Takao Fujiwara <fujiwara@redhat.com> 1.0.0.20211224-6
- Rename master_dic_file to main_dic_file

* Fri May 06 2022 Takao Fujiwara <fujiwara@redhat.com> 1.0.0.20211224-5
- Fix GCC_ANALYZER_WARNING with -Wanalyzer-null-dereference

* Fri Feb 11 2022 Takao Fujiwara <fujiwara@redhat.com> 1.0.0.20211224-4
- Resolves: #2051670 xemacs is a dead package

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.20211224-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 24 2021 Takao Fujiwara <fujiwara@redhat.com> 1.0.0.20211224-1
- Bump to 1.0.0.20211224-1

* Tue Oct 26 2021 Takao Fujiwara <fujiwara@redhat.com> 1.0.0.20201109-10
- Resolves: #1998727 Fix emacs-anthy-unicode

* Thu Oct 21 2021 Takao Fujiwara <fujiwara@redhat.com> 1.0.0.20201109-8
- Resolves: #2007482 Update gcanna.ctd with Shubitai

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.20201109-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Takao Fujiwara <fujiwara@redhat.com> 1.0.0.20201109-6
- Fix covscan report

* Mon Jul 12 2021 Takao Fujiwara <fujiwara@redhat.com> 1.0.0.20201109-5
- Fix covscan report

* Mon May 03 2021 Takao Fujiwara <fujiwara@redhat.com> 1.0.0.20201109-4
- Delete unnecessary xemacs in tests/tests.yml

* Sat May 01 2021 Takao Fujiwara <fujiwara@redhat.com> 1.0.0.20201109-3
- Enable CI

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.20201109-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 09 2020 Takao Fujiwara <fujiwara@redhat.com> 1.0.0.20201109-1
- Bump 1.0.0.20201109

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.20191015-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.20191015-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.20191015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 21 2019 Takao Fujiwara <fujiwara@redhat.com> 1.0.0.20191015-2
- Add %%check to run local test programs

* Tue Oct 15 2019 Takao Fujiwara <fujiwara@redhat.com> 1.0.0.20191015-1
- Release anthy-unicode 1.0.0.20191015

* Wed Aug 07 2019 Takao Fujiwara <fujiwara@redhat.com> 1.0.0.20190412-1
- Initial package
- Update license
- Delete Group tags
- Make parse_modify_freq_command() for UTF-8
- Revert ptab.h to EUC-JP
- BuildRequire: git
- Genearate emacs- and xemacs- sub packages
- Fix some obsolete warnings in emacs batch-byte-compile
- Fix shared-lib-calls-exit
- Fix non-conffile-in-etc
- Fix description-line-too-long
