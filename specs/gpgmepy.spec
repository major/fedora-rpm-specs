Name:           gpgmepy
Version:        2.0.0
Epoch:          1
Release:        4%{?dist}
Summary:        Python bindings for GPGME

# library LGPL-2.1-or-later, tests and examples use GPL-2.0-or-later
License:        LGPL-2.1-or-later
URL:            https://gnupg.org/related_software/gpgme/
Source0:        https://gnupg.org/ftp/gcrypt/%{name}/%{name}-%{version}.tar.bz2
Source1:        https://gnupg.org/ftp/gcrypt/%{name}/%{name}-%{version}.tar.bz2.sig
Source2:        https://gnupg.org/signature_key.asc

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  gpgverify
BuildRequires:  pkgconfig(gpgme) >= %{version}

%global _description %{expand:
Python bindings to the GPGME API of the GnuPG cryptography library.
}

%description %_description

%package -n python3-gpg
Summary:        %{summary}

%description -n python3-gpg %_description


%prep
# signing key for gpgmepy is different than for gpgme and unavailable atm
#{gpgverify} --keyring=%{SOURCE2} --signature=%{SOURCE1} --data=%{SOURCE0}
%autosetup -p1 -S gendiff

%generate_buildrequires
%pyproject_buildrequires


%build
# build script can't handle multiarch wrapper for gpgme.h used on some archs
%ifarch %{ix86} x86_64 ia64 ppc ppc64 s390 s390x %{sparc}
sed -i "s|^gpgme_h = ''|gpgme_h = '%{_includedir}/gpgme-%{__isa_bits}.h'|" setup.py.in
%endif
%configure
mv src gpg
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files gpg


%check
ln -s build python3-gpg
cd tests
make check

%files -n python3-gpg -f %{pyproject_files}
%doc AUTHORS ChangeLog NEWS README
%license COPYING*

%changelog
* Wed Jul 22 2026 Python Maint <python-maint@redhat.com> - 1:2.0.0-4
- Rebuilt for Python 3.15.0b4 ABI change

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Thu Jun 04 2026 Python Maint <python-maint@redhat.com> - 1:2.0.0-2
- Rebuilt for Python 3.15

* Mon May 04 2026 Michal Hlavinka <mhlavink@redhat.com> - 1:2.0.0-1
- initial build after gpgme split
