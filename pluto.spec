%global commit c6cab36140648828ccc72cc659d55d274508da0d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           pluto
Version:        0
Release:        0.18git%{shortcommit}%{?dist}
Summary:        Small utility library for SHA1, Tiny Encryption Algorithm, and UUID4

License:        GPLv3+
URL:            https://gitlab.com/CollectiveTyranny/pluto
Source0:	%{url}/-/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make

%description
%{summary}.

%package devel
Summary:        Development files and headers for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%package doc
Summary:        Documentation for %{name}-devel
BuildRequires:  doxygen
BuildRequires:  ghostscript
BuildRequires:  texlive-epstopdf
BuildArch:      noarch

%description doc
%{summary}.

%prep
%autosetup -n %{name}-%{commit}
mkdir %{_vpath_builddir}

%build
%cmake -B %{_vpath_builddir} .

%make_build -C %{_vpath_builddir}
%make_build doc -C %{_vpath_builddir}

%install
%make_install -C %{_vpath_builddir}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so

%files doc
%license LICENSE
%doc doc/html

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18gitc6cab36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17gitc6cab36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16gitc6cab36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15gitc6cab36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14gitc6cab36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 7 2020 Andy Mender <andymenderunix@fedoraproject.org> - 0-0.13gitc6cab36
- Make out-of-source build backwards compatible with Fedora 32

* Tue Nov 24 2020 Andy Mender <andymenderunix@fedoraproject.org> - 0-0.12gitc6cab36
- Add missing BuildRequires on texlive-epstopdf and ghostscript
- Improve Source0 field
- Switch to out-of-source cmake builds
- Replace %%ldconfig_scriplets with correct ldconfig calls

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11gitc6cab36
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10gitc6cab36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9gitc6cab36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8gitc6cab36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7gitc6cab36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6gitc6cab36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5gitc6cab36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4gitc6cab36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3gitc6cab36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2gitc6cab36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 27 2016 Igor Gnatenko <ignatenko@redhat.com> - 0-0.1gitc6cab36
- Initial package
