%global forgeurl https://github.com/pchev/libpasraw/

Version:        1.3.0
%forgemeta

Name:           libpasraw
Release:        11%{?dist}
Summary:        Pascal interface to libraw

License:        GPLv3+
URL:            %{forgeurl}
Source0:        %{forgesource}

# Patch to fix stripping of library files
# Since this is Fedora specific we don't ask upstream to include
Patch0:         libpasraw-1.3-nostrip.patch

# Add LDFLAGS to compiler
Patch1:         libpasraw-1.3-ldflags.patch


BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libraw)
BuildRequires: make

%description
Provides shared library to interface Pascal program with libraw.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}


%prep
%autosetup -p1

# do not install docs, use %%doc macro
sed -i '/\$destdir\/share/d' ./install.sh

# fix library path in install.sh script on 64bit
sed -i 's/\$destdir\/lib/\$destdir\/%{_lib}/g' ./install.sh

%build
%make_build arch_flags="%{optflags}" LDFLAGS="%{build_ldflags}"

%install
make install PREFIX=%{buildroot}%{_prefix}


%files
%license LICENSE
%doc changelog copyright README.md
%{_libdir}/%{name}.so.1
%{_libdir}/%{name}.so.1.1

%files devel
%{_libdir}/%{name}.so


%changelog
* Tue Dec 20 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.3.0-11
- LibRaw rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.3.0-5
- Rebuild for new LibRaw

* Mon Mar 16 2020 Mattia Verga <mattia.verga@protonmail.com> - 1.3.0-4
- Use %%make_build macro

* Mon Mar 16 2020 Mattia Verga <mattia.verga@protonmail.com> - 1.3.0-3
- Add -devel subpackage

* Sun Mar 15 2020 Mattia Verga <mattia.verga@protonmail.com> - 1.3.0-2
- Fix license file
- Use ldflags

* Sat Mar 07 2020 Mattia Verga <mattia.verga@protonmail.com> - 1.3-1.20200302gitdbbe4cc
- Initial packaging
