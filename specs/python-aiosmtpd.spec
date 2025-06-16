%global pkgname aiosmtpd
%global summary Asyncio-based SMTP server
%global _description \
This is a server for SMTP and related protocols, similar in utility \
to the standard library’s smtpd.py module, but rewritten to be based \
on asyncio for Python 3.
%global srcname %{pkgname}


Name:           python-%{pkgname}
Version:        1.4.4.post2
Release:        %autorelease
Summary:        %{summary}

License:        Apache-2.0
URL:            https://github.com/aio-libs/aiosmtpd
Source0:        %{url}/archive/%{version}/%{pkgname}-%{version}.tar.gz

# Proposed python3.13 test fix
# See https://github.com/aio-libs/aiosmtpd/pull/473
Patch0:         aiosmtpd-py313.patch
# Fix build against python3.14
# - Replace ByteString with bytearray
# https://github.com/aio-libs/aiosmtpd/pull/556
Patch1:         aiosmtpd-py3.14.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
# Required for tests
BuildRequires:  git-core

%description %{_description}


%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{pkgname} %{_description}


%prep
%autosetup -p1 -n %{srcname}-%{version}
# Remove unused cosmetic dependencies to tests
sed -i 's/pytest-print//' tox.ini
sed -i 's/pytest-sugar//' tox.ini
sed -i 's/pytest-profiling//' tox.ini
# Remove unused linter dependency
sed -i 's/bandit//' tox.ini

rm aiosmtpd/docs/.gitignore
rm examples/authenticated_relayer/.gitignore

%generate_buildrequires
%pyproject_buildrequires -t -e nocov


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files %{pkgname}


%check
%{__python3} -m pytest -v -k "not (unknown_args_ or factory_none or noexc_smtpd_missing)"
# %%tox


%files -n python%{python3_pkgversion}-%{pkgname} -f %{pyproject_files}
%license LICENSE
%doc README.rst examples
%{_bindir}/aiosmtpd


%changelog
%autochangelog
