Name:           virtme
Version:        0.1.1
Release:        21%{?dist}
Summary:        Virtualize the running distro or a simple rootfs

License:        GPLv2
URL:            https://git.kernel.org/cgit/utils/kernel/virtme/virtme.git/
Source0:        https://www.kernel.org/pub/linux/utils/kernel/virtme/releases/%{name}-%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  python3-devel python3-setuptools

Requires:       python3-setuptools

# virtme doesn't really need busybox, but it works better if busybox
# is available
Requires:       busybox

# virtme-guest is no longer necessary and therefore no longer exists
Obsoletes:      virtme-guest < 0.0.2-5

# Intentionally does not require qemu, since virtme can work with
# a number of qemu-system-arch packages.

%description
Virtme is a set of simple tools to run a virtualized Linux kernel that
uses the host Linux distribution or a simple rootfs instead of a whole
disk image.


%prep
%setup -q


%build
# If this ever adds C code, CFLAGS will be needed here.
%{__python3} setup.py build


%check
%{__python3} setup.py test


%install
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%files
%doc README.md
%license LICENSE
# For noarch packages: sitelib
%{python3_sitelib}/*
%{_bindir}/virtme-run
%{_bindir}/virtme-configkernel
%{_bindir}/virtme-mkinitramfs
%{_bindir}/virtme-prep-kdir-mods


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.1-20
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.1-17
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-14
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 10 2019 luto@kernel.org - 0.1.1-12
- New release (with wrong release number -- oops)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.3-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.3-11
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.3-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.0.3-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Feb 23 2016 luto@kernel.org - 0.0.3-1
- New release
- virtme-guest is obsolete

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 23 2014 Andy Lutomirski <luto@mit.edu> - 0.0.2-1
- New upstream version.

* Sun Sep  7 2014 Andy Lutomirski <luto@mit.edu> - 0.0.1-1
- New package.
