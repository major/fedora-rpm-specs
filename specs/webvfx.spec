Name:           webvfx
Version:        1.2.0
Release:        14%{?dist}
Summary:        Video effects engine based on web technologies
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/mltframework/webvfx
Source0:        https://github.com/mltframework/webvfx/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-libdir.patch

BuildRequires: make
#BuildRequires:  mlt-devel >= 6.20.0
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  doxygen
BuildRequires:  chrpath

%description
WebVfx is a video effects library that allows effects to be implemented using
WebKit HTML or Qt QML.

%package        devel
Summary:        Development library for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}

%description    devel
Development library for %{name}

%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains html documentation
that use %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{qmake_qt5} PREFIX=%{_prefix} LIB_SUFFIX=%{_lib} \
..
%make_build
popd

# update Doxyfile
doxygen -u doc/Doxyfile
# build docs
doxygen doc/Doxyfile

%install
%make_install INSTALL_ROOT=%{buildroot} -C %{_target_platform}

# Remove rpath
chrpath --delete %{buildroot}%{_bindir}/%{name}_viewer
chrpath --delete %{buildroot}%{_bindir}/%{name}_render
#chrpath --delete %{buildroot}%{_libdir}/mlt/libmltwebvfx.so

%ldconfig_scriptlets

%files
%doc README.md
%license LICENSE
%{_bindir}/webvfx_*
#%%{_libdir}/mlt/libmltwebvfx.so
%{_libdir}/libwebvfx.so.*

%files devel
%{_libdir}/libwebvfx.so

%files doc
%license LICENSE
%doc doxydoc

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.0-13
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb 09 2022 Sérgio Basto <sergio@serjux.com> - 1.2.0-7
- No support for MLT-7 https://fedoraproject.org/wiki/Changes/F36MLT-7

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 18 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 29 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Sat Aug 03 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-5
- Rebuilt

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 25 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-3
- Add %%{name}-qt512.patch to compile with qt-5.12

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-0.4.20160823gite918ce4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-0.3.20160823gite918ce4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 27 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.4.5-0.2.20160823gite918ce4
- Use development snapshot
- Remove Group tag
- Add doc subpkg
- Add BR doxygen

* Sat Sep 09 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.4.5-0.1.20160823gite918ce4
- Initial build.
