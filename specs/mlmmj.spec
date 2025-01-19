%global __requires_exclude perl\\(.*[.]pl\\)|\/bin\/bash
%global modulename mlmmj
%global selinuxtype targeted

Name:           mlmmj
Version:        1.4.7
Release:        2%{?dist}
Summary:        A simple and slim mailing list manager inspired by ezmlm
License:        MIT
URL:            https://codeberg.org/mlmmj/mlmmj
Source0:        https://codeberg.org/%{name}/%{name}/releases/download/%{name}-%{version}.tar.gz
Source1:        %{modulename}.te
Source2:        %{modulename}.fc
Source3:        README.SELinux

BuildRequires:  gcc
BuildRequires:  findutils
BuildRequires:  kyua
BuildRequires:  libatf-c-devel
BuildRequires:  libatf-sh-devel
BuildRequires:  make

%description
Mlmmj(Mailing List Management Made Joyful) is a simple and slim mailing list 
manager (MLM) inspired by ezmlm. It works with many different Mail Transport 
Agents (MTAs) and is simple for a system adminstrator to install, configure 
and integrate with other software. As it uses very few resources, and requires
no daemons, it is ideal for installation on systems where resources are 
limited, such as Virtual Private Servers (VPSes).

Although it doesn't aim to include every feature possible, but focuses on 
staying mean and lean, and doing what it does do well, it does have a great 
set of features, including:

- Archive
- Custom headers / footer
- Fully automated bounce handling (similar to ezmlm)
- Complete requeueing functionality
- Moderation functionality
- Subject prefix
- Subscribers only posting
- Regular expression access control
- Functionality to retrieve old posts
- Web interface
- Digests
- No-mail subscription
- VERP support
- Delivery Status Notification (RFC1891) support
- Rich, customisable texts for automated operations

%package        selinux
Summary:        SELinux support for mlmmj
BuildArch:      noarch
Requires:       %{name} = %{version}
Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
BuildRequires:  selinux-policy-devel

%description selinux
This package adds SELinux enforcement support to mlmmj.

%prep
%autosetup
# SELinux
mkdir selinux
cp -p %{SOURCE1} selinux/%{modulename}.te
cp -p %{SOURCE2} selinux/%{modulename}.fc
cp -p %{SOURCE3} selinux/README.SELinux
touch selinux/%{modulename}.if

%build
%configure --enable-receive-strip
%make_build
# SELinux
make -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp
bzip2 -9 %{modulename}.pp

%install
%make_install

mkdir -p %{buildroot}%{_localstatedir}/spool/%{name}
find contrib/ -type f -name *.pl -exec chmod -x {} ";"
find contrib/ -type f -name *.cgi -exec chmod -x {} ";"

# SELinux
install -D -m 0644 %{modulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2

%pre
getent group mlmmj &>/dev/null || %{_sbindir}/groupadd -r mlmmj
getent passwd mlmmj &>/dev/null || \
    %{_sbindir}/useradd -r -g mlmmj -s /sbin/nologin -c "mlmmj user" -d %{_localstatedir}/spool/%{name} mlmmj

%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}

%files
%license COPYING
%doc AUTHORS ChangeLog FAQ README* TODO TUNABLES.md UPGRADE
%doc contrib/web/
%{_bindir}/*
%{_mandir}/man1/mlmmj*.1*
%{_datadir}/%{name}/
%dir %attr(0700,mlmmj,root) %{_localstatedir}/spool/%{name}

%files selinux
%doc selinux/README.SELinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.*
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{modulename}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 21 2024 Denis Fateyev <denis@fateyev.com> - 1.4.7-1
- Update to 1.4.7 release

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Apr 22 2024 Denis Fateyev <denis@fateyev.com> - 1.4.5-2
- Added packages to build dependencies

* Tue Mar 26 2024 Denis Fateyev <denis@fateyev.com> - 1.4.5-1
- Update to 1.4.5 release

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 12 2024 Denis Fateyev <denis@fateyev.com> - 1.4.4-1
- Update to 1.4.4 release
- Change upstream parameters

* Mon Dec 04 2023 Denis Fateyev <denis@fateyev.com> - 1.3.0-17
- Add system user and group assignment
- Add initial SELinux support

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 28 2020 Denis Fateyev <denis@fateyev.com> - 1.3.0-9
- Add "legacy_common_support" build option

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 29 2017 Denis Fateyev <denis@fateyev.com> - 1.3.0-1
- Update to 1.3.0 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 02 2016 Denis Fateyev <denis@fateyev.com> - 1.2.19.0-1
- Update to 1.2.19.0 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Christopher Meng <rpm@cicku.me> - 1.2.18.1-1
- Update to 1.2.18.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.18.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Oct 26 2013 Christopher Meng <rpm@cicku.me> - 1.2.18.0-2
- Filter out wrong dependencies.

* Fri Aug 09 2013 Christopher Meng <rpm@cicku.me> - 1.2.18.0-1
- Resubmit the package.
