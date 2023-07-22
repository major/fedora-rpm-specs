# git ls-remote git://github.com/g0orx/linhpsdr.git
%global git_commit 742658a9068392349ca1efc9d698dcaae541dda6
%global git_date 20210710

# git describe --abbrev=0 --tags
%global version_tag Beta
# git --no-pager show --date=short --format="%ai" --name-only | head -n 1 | cut -d' ' -f1
%global version_date 2021-02-25

%global features \\\
  SOAPYSDR_INCLUDE=SOAPYSDR

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:		linhpsdr
Version:	0
Release:	0.6.%{git_suffix}%{?dist}
Summary:	An HPSDR application for Linux
License:	GPLv2+
URL:		https://github.com/g0orx/%{name}
Source0:	%{url}/archive/%{git_commit}/%{name}-%{git_suffix}.tar.gz
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	gtk3-devel
BuildRequires:	libsoundio-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	SoapySDR-devel
BuildRequires:	unixcw-devel
BuildRequires:	wdsp-devel
BuildRequires:	desktop-file-utils
Requires:	hicolor-icon-theme
# https://github.com/g0orx/linhpsdr/pull/107
Patch0:		linhpsdr-0-distro-makefile.patch

%description
An HPSDR (High Performance Software Defined Radio) application for controlling
HPSDR compatible radios, e.g. Orion, Angelia, Hermes, ...

%package doc
Summary:	Documentation files for linhpsdr
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation files for linhpsdr.

%prep
%autosetup -n %{name}-%{git_commit} -p1

%build
%make_build CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" \
  GIT_VERSION="%{version_tag}" GIT_DATE="%{version_date}" %{features}

%install
%make_install BINDIR="%{buildroot}%{_bindir}" DATADIR="%{buildroot}%{_datadir}" %{features}

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*

%files doc
%doc documentation/*.pdf

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20210710git742658a9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20210710git742658a9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20210710git742658a9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20210710git742658a9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep  8 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.2.20210710git742658a9
- Updated description according to the review
  Related: rhbz#1981048

* Sat Jul 10 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.1.20210710git742658a9
- Initial release
