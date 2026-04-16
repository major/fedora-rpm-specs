Name:           python-passlib
Version:        1.9.3
Release:        %autorelease
Summary:        Comprehensive password hashing framework supporting over 20 schemes

# license breakdown is described in LICENSE file
License:        BSD-3-Clause AND Beerware AND UnixCrypt AND ISC
URL:            https://github.com/notypecheck/passlib
Source:         %pypi_source libpass

BuildArch:      noarch

# docs generation requires python-cloud-sptheme, which isn't packaged yet.
# so we won't generate the docs yet.
#BuildRequires: python2-sphinx >= 1.0
#BuildRequires: python2-cloud-sptheme

%global _description %{expand:
Passlib is a password hashing library for Python 2 & 3, which provides
cross-platform implementations of over 20 password hashing algorithms,
as well as a framework for managing existing password hashes. It is
designed to be useful for a wide range of tasks, from verifying a hash
found in /etc/shadow, to providing full-strength password hashing for
multi-user application.}


%description %{_description}


%package -n python3-passlib
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest


%description -n python3-passlib %{_description}


# el9 missing argon2 https://bugzilla.redhat.com/show_bug.cgi?id=2089340
%pyproject_extras_subpkg -n python3-passlib %{!?el9:argon2} bcrypt totp


%prep
%autosetup -p1 -n libpass-%{version}

%generate_buildrequires
%pyproject_buildrequires -x bcrypt -x totp %{!?el9:-x argon2} 


%build
%pyproject_wheel
# This package was renamed from passlib to libpass and we want to provide the old distinfo
# for packages that still need it.
%global legacy_distinfo passlib-%{version}.dist-info
mkdir %{legacy_distinfo}
cat > %{legacy_distinfo}/METADATA << EOF
Metadata-Version: 2.1
Name: passlib
Version: %{version}
EOF
echo rpm > %{legacy_distinfo}/INSTALLER


%install
%pyproject_install
%pyproject_save_files -l passlib

cp -a %{legacy_distinfo} %{buildroot}%{python3_sitelib}


%check
%pytest

%{py3_test_envvars} %{python3} -c 'import importlib.metadata as im; assert im.version("passlib") == im.version("libpass") == "%{version}"'


%files -n python3-passlib -f %{pyproject_files}
%doc README.md
%{python3_sitelib}/%{legacy_distinfo}/


%changelog
%autochangelog
