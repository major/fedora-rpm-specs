%global pkg rinari
%global pkgname Rinari

Name:             emacs-rinari
Version:          2.1  
Release:          33.20100815git%{?dist}
Summary:          Ruby on rails minor mode for Emacs

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:          GPL-3.0-or-later
URL:              http://rinari.rubyforge.org/

# The source of this package was pulled from upstream's vcs.
# use the following command to generate the tar ball:
# git clone http://github.com/eschulte/rinari.git
# cd rinari
# git submodule init
# git submodule update
# cd ..
# tar cvjf rinari-20100805.tar.bz2 rinari/

Source0:          http://sagarun.fedorapeople.org/misc/rinari-20100815.tar.bz2
Source1:          emacs-rinari-init.el

BuildRequires:    emacs texinfo
BuildArch:        noarch
Requires:         emacs(bin) >= %{_emacs_version}

Obsoletes:        %{name}-el < 2.1-30.20100815git
Provides:         %{name}-el = %{version}-%{release}

%description
Rinari is a set of Emacs Lisp functions aimed towards 
making Emacs into a top-notch Ruby on rails development environment.

%prep
%setup -q -n %{pkg}

%build
/usr/bin/emacs -batch --no-init-file --no-site-file --eval '(progn (normal-top-level-add-subdirs-to-load-path))' -f batch-byte-compile *.el
%{_emacs_bytecompile} util/*el
%{_emacs_bytecompile} util/jump/*.el
makeinfo doc/rinari.texi


%install
rm -rf %{buildroot}
install -pm 755 -d  %{buildroot}%{_emacs_sitelispdir}/%{pkg}/
install -pm 644 *.el* %{buildroot}%{_emacs_sitelispdir}/%{pkg}/
install -pm 755 -d %{buildroot}%{_emacs_sitelispdir}/%{pkg}/util/
install -pm 644 util/*.el* %{buildroot}%{_emacs_sitelispdir}/%{pkg}/util/
install -pm 755 -d %{buildroot}%{_emacs_sitelispdir}/%{pkg}/util/jump/
install -pm 644 util/jump/*.el* %{buildroot}%{_emacs_sitelispdir}/%{pkg}/util/jump/
install -pm 755 -d %{buildroot}%{_infodir}
install -pm 644 doc/%{pkg}.info %{buildroot}%{_infodir}/
install -pm 755 -d %{buildroot}%{_emacs_sitestartdir}/
install -pm 644 %{SOURCE1} %{buildroot}%{_emacs_sitestartdir}/

%files
%doc TODO README
%{_emacs_sitelispdir}/%{pkg}/*.el
%{_emacs_sitelispdir}/%{pkg}/*.elc
%{_emacs_sitelispdir}/%{pkg}/util/*.el
%{_emacs_sitelispdir}/%{pkg}/util/*.elc
%{_emacs_sitelispdir}/%{pkg}/util/jump/*.el
%{_emacs_sitelispdir}/%{pkg}/util/jump/*.elc
%{_infodir}/%{pkg}.info.*
%{_emacs_sitestartdir}/emacs-rinari-init.el
%dir %{_emacs_sitelispdir}/%{pkg}/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-33.20100815git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1-32.20100815git
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-31.20100815git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 15 2024 Tim Landscheidt <tim@tim-landscheidt.de> - 2.1-30.20100815git
- Obsolete -el subpackage (#1234531)
- Remove obsolete requirements for post/preun scripts

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-29.20100815git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-28.20100815git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-27.20100815git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-26.20100815git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-25.20100815git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-24.20100815git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-23.20100815git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-22.20100815git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-21.20100815git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-20.20100815git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-19.20100815git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 2.1-18.20100815git
- Remove hardcoded gzip suffix from GNU info pages

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-17.20100815git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-16.20100815git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-15.20100815git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-14.20100815git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-13.20100815git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-12.20100815git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-11.20100815git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-10.20100815git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-9.20100815git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-8.20100815git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-7.20100815git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-6.20100815git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-5.20100815git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 15 2010 Arun SAG <sagarun at gmail dot com> - 2.1-4.20100815git
- Includes all directories under rinari directory.

* Sun Aug 15 2010 Arun SAG <sagarun at gmail dot com> - 2.1-3.20100815git
- Fixed the global package name macro.
- Removed redundant directory ownerships.
- Removed quotes from the summary.

* Sun Aug 15 2010 Arun SAG <sagarun at gmail dot com> - 2.1-2.20100815git
- Removed patch0 as it is now integrated into the mainline code.
- Corrected source URL.
- Corrected comments to improve readability.
- Nouns in summary are enclosed in double quotes.
- Emacs addon's packaging template is now honored.
- Ido mode is not enabled by default.

* Tue Aug 3 2010 Arun SAG <sagarun at gmail dot com> - 2.1-1.20100805git
- Initial release. 
