Name:             mpc
Summary:          Command-line client for MPD
Version:          0.35
Release:          6%{?dist}

License:          GPL-2.0-or-later
URL:              http://www.musicpd.org/
Source0:          http://www.musicpd.org/download/mpc/0/mpc-%{version}.tar.xz
BuildRequires:    bash-completion
BuildRequires:    libmpdclient-devel >= 2.3
BuildRequires:    meson
BuildRequires:    python3-sphinx
BuildRequires:    gcc
BuildRequires:    rsync

%description
A client for MPD, the Music Player Daemon. mpc connects to a MPD running
on a machine via a network.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
install -p -D -m0644 contrib/mpc-completion.bash %{buildroot}%{bash_completions_dir}/%{name}
for i in mpd-m3u-handler.sh mpd-pls-handler.sh; do
    install -p -D -m0755 %{buildroot}%{_datadir}/doc/%{name}/contrib/${i} \
        %{buildroot}%{_libexecdir}/%{name}/${i}
done
rm -rf %{buildroot}%{_pkgdocdir}/contrib
rm -f %{buildroot}%{_pkgdocdir}/COPYING
rm -f %{buildroot}%{_pkgdocdir}/html/.buildinfo


%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{bash_completions_dir}/%{name}
%{_libexecdir}/%{name}
%{_pkgdocdir}


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Sep 15 2024 Pavel Solovev <daron439@gmail.com> - 0.35-5
- Fix FTBFS

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 29 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 0.35-1
- Update to 0.35

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 13 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 0.34-1
- Update to 0.34

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 29 2020 Todd Zullinger <tmz@pobox.com> - 0.33-3
- Update bash-completion path

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Vasiliy Glazov <vascom2@gmail.com> - 0.33-1
- Update to 0.33

* Tue Jul 30 2019 Vasiliy Glazov <vascom2@gmail.com> - 0.32-1
- Update to 0.32

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 18 2018 Adrian Reber <adrian@lisas.de> - 0.30-3
- Added BR: gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 03 2018 Adrian Reber <adrian@lisas.de> - 0.30-1
- updated to 0.30
- switched to meson build system

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Adrian Reber <adrian@lisas.de> - 0.28-5
- Rebuilt for new libmpdclient

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 30 2016 Adrian Reber <adrian@lisas.de> - 0.28-1
- updated to 0.28

* Sun Feb 28 2016 Adrian Reber <adrian@lisas.de> - 0.27-1
- updated to 0.27

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 07 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.26-1
- update to upstream release 0.26

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 23 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.25-1
- update to upstream release 0.25
- update URL
- remove INSTALL file

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 24 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.22-4
- install bash completion in the correct place and remove the
  triggerin/triggerun scriptlets
- include the example scripts in libexecdir

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 21 2012 Jamie Nguyen <jamie@tomoyolinux.co.uk> - 0.22-1
- update to upstream release 0.22
- remove obsolete BuildRoot tag, %%clean section and %%defattr

* Thu Jan 28 2010 Adrian Reber <adrian@lisas.de> - 0.19-1
- updated to 0.19 (#543797)
- added BR libmpdclient-devel

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 16 2009 Adrian Reber <adrian@lisas.de> - 0.16-1
- updated to 0.16

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Adrian Reber <adrian@lisas.de> - 0.15-1
- updated to 0.15 (#486585)

* Tue Feb 12 2008 Adrian Reber <adrian@lisas.de> - 0.12.1-2
- rebuilt for gcc43

* Sun Aug 26 2007 Adrian Reber <adrian@lisas.de> - 0.12.1-1
- updated to 0.12.1
- updated License
- added BR gawk

* Wed Jan 31 2007 Adrian Reber <adrian@lisas.de> - 0.12.0-2
- fix for almost empty debuginfo package (bz #225103)

* Tue Nov 07 2006 Adrian Reber <adrian@lisas.de> - 0.12.0-1
- updated to 0.12.0

* Wed Aug 30 2006 Aurelien Bompard <abompard@fedoraproject.org> 0.11.2-5
- rebuild

* Tue Feb 21 2006 Aurelien Bompard <gauret[AT]free.fr> 0.11.2-4
- rebuild for FC5

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.11.2-3
- rebuild on all arches

* Fri Apr 08 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sat Mar 12 2005 Aurelien Bompard <gauret[AT]free.fr> 0.11.2-1
- version 0.11.2
- drop Epoch
- update URL

* Wed Dec 08 2004 Aurelien Bompard <gauret[AT]free.fr> 0:0.11.1-2
- put the bash_completion file in %%_datadir instead of %%_docdir

* Fri Nov 05 2004 Aurelien Bompard <gauret[AT]free.fr> 0:0.11.1-0.fdr.1
- Adapted to Fedora's spec directions.

* Wed Jun 23 2004 Gary Peck <gbpeck@sbcglobal.net> 0.11.1-1
- Version 0.11.1

