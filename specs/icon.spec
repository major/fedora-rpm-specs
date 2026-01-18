%global git_user0 gtownsend

Name:           icon
Version:        9.5.24b
Release:        3%{?dist}
Summary:        Icon programming language
License:        LicenseRef-Fedora-Public-Domain
URL:            https://www2.cs.arizona.edu/icon/
Source0:        https://github.com/%{git_user0}/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz

# Fedora-specific patch to avoid stripping executables
Patch0:         icon-nostrip.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xpm)


%global _description %{expand:
Icon is a high-level general-purpose programming language with novel features
including string scanning and goal-directed evaluation.}

%description %_description


%package utils
Summary:        Icon utility programs
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description utils %_description


%prep
%autosetup -p1 -n %{name}-%{version}

%build
make X-Configure name=linux
# The Makefile does not explicitly set an -std flag. The code makes use
# of some constructs that are rejected when compiling in gnu23 mode (default
# in GCC15). It'd be better to patch those properly, but for now, this'll do.
sed -i -e 's|CFLAGS = -O|CFLAGS = %{optflags} -std=gnu99|' Makedefs
sed -i -e 's|Igpx|Xpm|' Makedefs

# NOTE: make fails if smp_mflags is used
make -j1 All

%check
make Test

%install
# the icon "make Install" assumes the use of an icon-specific tree,
# while we want to put the binaries in the system binary directory,
# but the libraries in lib/icon.

# binaries
install -d -m0755 %{buildroot}%{_bindir}
install -p -m0755 bin/icon[tx] %{buildroot}%{_bindir}
ln -s icont %{buildroot}%{_bindir}/icon

# includes
# Since there's only one small file, it doesn't make sense to create a
# separate icon-devel package
install -d -m0755 %{buildroot}%{_includedir}
install -p -m0644 lib/icall.h %{buildroot}%{_includedir}

# libraries
install -d -m0755 %{buildroot}%{_libdir}/%{name}
install -p -m0644 -s bin/libcfunc.so %{buildroot}%{_libdir}/%{name}
install -p -m0644 lib/*.icn lib/*.u[12] %{buildroot}%{_libdir}/%{name}

# man pages
install -d -m0755 %{buildroot}%{_mandir}/man1
install -p -m0644 man/man1/* %{buildroot}%{_mandir}/man1

# utility binaries
install -p -m0755 bin/[cfpvw]* %{buildroot}%{_bindir}
# xgamma conflicts with same named executable from xorg-x11-server-utils,
# so rename
install -p -m0755 bin/xgamma %{buildroot}%{_bindir}/icon-xgamma

%files
# rpmlint will give errors regarding some libdir/icon/*.u1 files being
# zero-length, but that is correct.
%license README
%{_bindir}/icon
%{_bindir}/icon[tx]
%{_includedir}/icall.h
%{_libdir}/%{name}
%{_mandir}/man1/*.1*
%doc doc/*

%files utils
%{_bindir}/[cfpvw]*
%{_bindir}/icon-xgamma


%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.24b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.24b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri May 23 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 9.5.24b-1
- Update to v9.5.24b

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.20i-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.20i-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.20i-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.20i-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.20i-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.20i-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.20i-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.20i-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.20i-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.20i-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Sep 13 2020 Eric Smith <brouhaha@fedoraproject.org> 9.5.20i-1
- Update to latest upstream.

* Sat Sep 12 2020 Eric Smith <brouhaha@fedoraproject.org> 9.5.20h-2
- Use system libXpm rather than bundled.

* Sun Aug 02 2020 Eric Smith <brouhaha@fedoraproject.org> 9.5.20h-1
- Initial version.
