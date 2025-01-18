Name:           editline
Version:        1.17.1
Release:        12%{?dist}
Summary:        A small compatible replacement for readline

# https://fedoraproject.org/wiki/Licensing/Henry_Spencer_Reg-Ex_Library_License
# also cf https://www.openhub.net/licenses/cnews
License:        Spencer-94
URL:            https://troglobit.com/projects/editline/
Source0:        https://github.com/troglobit/editline/releases/download/%{version}/editline-%{version}.tar.xz
BuildRequires:  gcc
BuildRequires: make

%description
This is a line editing library for UNIX. It can be linked into almost
any program to provide command line editing and history. It is call
compatible with the FSF readline library, but is a fraction of the
size (and offers fewer features).


%package devel
Summary:        Development files for editline
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for the editline library.


%prep
%autosetup


%build
%configure --disable-static
%make_build


%install
%make_install

rm %{buildroot}/%{_libdir}/libeditline.la
rm %{buildroot}/%{_docdir}/editline/{LICENSE,README.md}
rm %{buildroot}/%{_mandir}/man3/editline.3


%files
%license LICENSE
%{_libdir}/libeditline.so.1
%{_libdir}/libeditline.so.1.0.2


%files devel
%doc ChangeLog.md README.md
%{_includedir}/editline.h
%{_libdir}/libeditline.so
%{_libdir}/pkgconfig/libeditline.pc
# conflicts with libedit-devel
#%%{_mandir}/man3/editline.3.gz


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 13 2020 Jens Petersen <petersen@redhat.com> - 1.17.1-2
- correct license is revised HSRL (#1867290)
- use isa for devel base requires (#1867290)

* Thu Aug 06 2020 Jens Petersen <petersen@redhat.com> - 1.17.1-1
- initial packaging
