%global icondir %{_datadir}/icons/hicolor
%global reponame danmaQ

Name:		danmaq
Version:	0.2.3.2
Release:	15%{?dist}
Summary:	A small client side Qt program to play danmaku on any screen

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		https://github.com/TUNA/%{reponame}
Source0:        %{url}/archive/v%{version}/%{reponame}-v%{version}.tar.gz

BuildRequires:	qt5-qtx11extras-devel
BuildRequires:	qt5-qtbase-devel
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:  libXext-devel

%description
DanmaQ is a small client side Qt program to play danmaku on any screen.

%prep
%setup -q -n %{reponame}-%{version}

%build
mkdir build && cd build
%cmake3 ..
# Since 0.2.3 it cannot be built in parallel. So use make instead of macro.
%cmake_build

%install
# install 
pushd build
%cmake_install
#install -Dm 0755 build/src/%{reponame} %{buildroot}%{_bindir}/%{reponame}
popd

# icon files
install -Dm0644 src/icons/statusicon.ico    %{buildroot}%{_datadir}/pixmaps/statusicon.ico
install -Dm0644 src/icons/statusicon.png    %{buildroot}%{_datadir}/pixmaps/statusicon.png
install -Dm0644 src/icons/statusicon_disabled.png    %{buildroot}%{_datadir}/pixmaps/statusicon_disabled.png
install -Dm0644 src/icons/statusicon.svg %{buildroot}%{icondir}/scalable/apps/statusicon.svg
install -Dm0644 src/resource/danmaQ.desktop %{buildroot}%{_datadir}/applications/%{reponame}.desktop
install -Dm0644 src/resource/danmaQ.png    %{buildroot}%{_datadir}/pixmaps/danmaQ.png
install -Dm0644 src/resource/danmaQ.svg %{buildroot}%{icondir}/scalable/apps/danmaQ.svg


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{reponame}.desktop

%post
/bin/touch --no-create %{_datadir}/icons/scalable &>/dev/null ||:

%postun
if [ $1 -eq 0 ]; then
  /bin/touch --no-create %{_datadir}/icons/scalable &>/dev/null ||:
  /usr/bin/gtk-update-icon-cache %{_datadir}/icons/scalable &>/dev/null ||:
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/scalable &>/dev/null ||:

%files
%doc README.md
%license LICENSE
%{_bindir}/%{reponame}
%{_mandir}/man1/%{reponame}.1.gz
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/%{reponame}.desktop

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.3.2-14
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Zamir SUN <sztsian@gmail.com> - 0.2.3.2-4
- Fix FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Zamir SUN <sztsian@gmail.com> - 0.2.3.2-1
- Fix FTBFS in Fedora 33
- Update to 0.2.3.2

* Sun Feb 09 2020 Zamir SUN <sztsian@gmail.com> - 0.2.3.1-8
- Fix FTBFS in Fedora 32
- Resolves 1799269

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.3.1-2
- Remove obsolete scriptlets

* Sun Nov 19 2017 Zamir SUN <zsun@fedoraproject.org> - 0.2.3.1-1
- Update to upstream version 0.2.3.1

* Sat Jul 29 2017 Zamir SUN <zsun@fedoraproject.org> - 0.2-1
- Change version to newest upstream tag

* Sat Jul 15 2017 Zamir SUN <zsun@fedoraproject.org> - 0-0.1.20170715git
- Initial with danmaQ git ab838667d53c71c6cf8ac94dd109fcd009460530
