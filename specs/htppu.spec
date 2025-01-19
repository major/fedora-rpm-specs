Summary: Hessu's Tampa Ping-Pong conversd URO modified version
Name: htppu
Version: 1.8
Release: 11%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://sourceforge.net/projects/htppu/
Source0: https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires: findutils
BuildRequires: gcc
BuildRequires: make
Patch0: htppu-1.8-install-fix.patch

%description
The URO modified Ping-Pong conversd, derived from WAMPES' conversd
by Dieter Deyke <deyke@mdddhd.fc.hp.com>. It is also used in
the Internet for ham radio conversation groups.

%prep
%setup -q

# remove execute permissions from everything
find . -type f -exec chmod a-x {} \;

%autopatch -p1

%build
%make_build COPTS="-DWANT_LOG %{optflags}" LDFLAGS="%{?__global_ldflags}"

%install
make install-all BASE_DIR="%{buildroot}" MAN_DIR="%{buildroot}%{_mandir}" LOG_DIR="%{buildroot}/var/log" \
  SBIN_DIR="%{buildroot}%{_sbindir}" OWN="root"

# docs
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a doc/* %{buildroot}%{_docdir}/%{name}
rm -f %{buildroot}%{_docdir}/%{name}/INSTALL

%files
%doc %{_docdir}/%{name}
%dir %{_sysconfdir}/htppu
%{_sbindir}/*
%config(noreplace) %{_sysconfdir}/htppu/*
%{_mandir}/*/*
%{_var}/lib/htppu

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.8-10
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar  9 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.8-1
- Initial release
