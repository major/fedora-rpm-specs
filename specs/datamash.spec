# Location for bash completions.  define, not global, is for lazy expansion.
# On el6, which doesn't have pkg-config for bash-completion,
# /etc/bash_completion.d seems to be the correct location, with a
# lot of entries symlinked from /usr/share/bash-completion.
%define compdir %(pkg-config --exists bash-completion &&
pkg-config --variable=completionsdir bash-completion ||
echo %_sysconfdir/bash_completion.d)

Name:           datamash
Version:        1.8
Release:        7%{?dist}
Summary:        A statistical, numerical and textual operations tool

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/%{name}/
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gettext perl(Digest::MD5) perl(Digest::SHA) perl(Data::Dumper)
BuildRequires:  perl(FileHandle) perl(File::Compare) perl(File::Find)
BuildRequires:  pkgconfig bash-completion
BuildRequires:  make
BuildRequires:  texinfo

%description
GNU datamash is a command-line program which performs basic
numeric,textual and statistical operations on input textual data
files.

%prep
%setup

# work around upstream gnulib issue that break ppc64le
# cf. https://bugzilla.redhat.com/show_bug.cgi?id=2056736#c10
rm lib/error.*


%build
%configure
%make_build

%install
%make_install
%{__rm} -f %{buildroot}/%{_infodir}/dir
%find_lang %{name}
%{__mkdir_p} %{buildroot}%{compdir}
%{__mv} %{buildroot}%{_datadir}/datamash/bash-completion.d/datamash %{buildroot}%{compdir}
# E: non-executable-script /usr/share/bash-completion/completions/datamash 644 /bin/bash
%{__sed} -i '/^#!/,1d' %{buildroot}%{compdir}/datamash

%check
%{__make} check

%post
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :

%preun
if [ $1 = 0 ];then
/sbin/install-info –delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%files -f %{name}.lang
%{_bindir}/*
%{_datadir}/datamash/
%{_infodir}/datamash.info.*
%dir %{compdir}/..
%dir %{compdir}
%{compdir}/datamash

%license COPYING
%doc README NEWS THANKS AUTHORS ChangeLog
%{_mandir}/man1/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.8-6
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Apr 02 2023 Georg Sauthoff <mail@gms.tf> - 1.8-1
- bump to upstream 1.8
- remove epel6 support (since it's EOL since Nov 2020)
- remove armv7hl patch since upstream fixed the format specifier (and armv7hl is EOL after f36)
- future proof shell bang line removal

* Sun Feb 12 2023 Filipe Rosset <rosset.filipe@gmail.com> - 1.7-5
- Remove obsolete requirements for %%post/%%preun scriptlets

* Thu Feb 02 2023 Sérgio Basto <sergio@serjux.com> - 1.7-4
- (#2056736) Fix FTBS on F37

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Feb 21 2022 Jirka Hladky <hladky.jiri@gmail.com> - 1.7-1
- New upstream release 1.7

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 28 2020 Jeff Law <law@redhat.com> - 1.6-5
- Re-enable LTO now that upstream GCC bugs have been fixed

* Mon Aug 10 2020 Jeff Law <law@redhat.com> - 1.6-4
- Disable LTO for now.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 22 2020 Filipe Rosset <rosset.filipe@gmail.com> - 1.6-1
- Update to 1.6

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 27 2019 Jirka Hladky <hladky.jiri@gmail.com> - 1.5-1
- New upstream release 1.5

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 1.3-4
- Remove hardcoded gzip suffix from GNU info pages

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 15 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.3-1
- new upstream release 1.3
- added upstream patch to fix tests on some platforms

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 05 2017 Hannes Frederic Sowa <hannes@stressinduktion.org> - 1.2-1
- new upstream release 1.2-1

* Fri Jun 30 2017 Hannes Frederic Sowa <hannes@stressinduktion.org> 1.1.1-1
- Initial version of the package
