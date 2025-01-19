%global debug_package %{nil}
%global commit 8e1c0a5699c34bc4952e86dc0509070770f2c625

Name:           mum-hash
Version:        0
Release:        10.20210318git%{commit}%{?dist}
Summary:        Fast non-cryptographic hash function

License:        MIT
URL:            https://github.com/vnmakarov/mum-hash
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

%define common_desc MUM hash is a fast non-cryptographic hash function suitable for \
different hash table implementations.

%description
%{common_desc}

%package  devel
Summary:  %{summary}
Provides: mum-hash-static = %{version}-%{release}

%description devel
%{common_desc}

%prep
%autosetup -n %{name}-%{commit}

%build

%install
mkdir -p %{buildroot}%{_includedir}
install -p -m 644 mum.h %{buildroot}%{_includedir}
install -p -m 644 mum-prng.h %{buildroot}%{_includedir}
install -p -m 644 mum512.h %{buildroot}%{_includedir}

%files devel
%doc README.md ChangeLog
%{_includedir}/mum*h

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-10.20210318git8e1c0a5699c34bc4952e86dc0509070770f2c625
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-9.20210318git8e1c0a5699c34bc4952e86dc0509070770f2c625
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-8.20210318git8e1c0a5699c34bc4952e86dc0509070770f2c625
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20210318git8e1c0a5699c34bc4952e86dc0509070770f2c625
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-6.20210318git8e1c0a5699c34bc4952e86dc0509070770f2c625
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-5.20210318git8e1c0a5699c34bc4952e86dc0509070770f2c625
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.20210318git8e1c0a5699c34bc4952e86dc0509070770f2c625
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-3.20210318git8e1c0a5699c34bc4952e86dc0509070770f2c625
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-2.20210318git8e1c0a5699c34bc4952e86dc0509070770f2c625
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 18 2021 Timothée Floure <fnux@fedoraproject.org> - 0-1.20210318git8e1c0a5
- Let there be package.
