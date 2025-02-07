Name:             python-alembic
Version:          1.14.1
Release:          %autorelease
Summary:          Database migration tool for SQLAlchemy

# SPDX
License:          MIT
URL:              https://pypi.io/project/alembic
Source0:          %{pypi_source alembic}

# Specific to Fedora: The tzdata Python package is essentially just a copy of
# the main tzdata package, we don’t need to have it.
Patch:            python-alembic-1.14.1-no-tzdata-pkg.patch

BuildArch:        noarch

BuildRequires:    help2man

BuildRequires:    python3-devel
BuildRequires:    python3-pytest
%if %{undefined rhel}
BuildRequires:    python3-pytest-xdist
%endif

BuildRequires:    tzdata

%global _description %{expand:
Alembic is a database migrations tool written by the author of SQLAlchemy. A
migrations tool offers the following functionality:

• Can emit ALTER statements to a database in order to change the structure of
  tables and other constructs
• Provides a system whereby "migration scripts" may be constructed; each script
  indicates a particular series of steps that can "upgrade" a target database
  to a new version, and optionally a series of steps that can "downgrade"
  similarly, doing the same steps in reverse.
• Allows the scripts to execute in some sequential manner.

Documentation and status of Alembic is at https://alembic.sqlalchemy.org/}

%description %_description


%package -n python3-alembic
Summary:          %summary

%description -n python3-alembic %_description


# Don’t use the %%pyproject_extras_subpkg macro, we want it to depend on the
# main tzdata package, not python3dist(tzdata) (which we don’t have).

%package -n python3-alembic+tz
Summary: Metapackage for python3-alembic: tz extra
Requires: python3-alembic = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: tzdata

%description -n python3-alembic+tz
This is a metapackage bringing in tz extra requires for python3-alembic.
It contains no code, just makes sure the dependencies are installed.


%prep
%autosetup -p1 -n alembic-%{version}
# HTML documentation has bundled and pre-compiled/pre-minified JavaScript; see
# https://docs.fedoraproject.org/en-US/packaging-guidelines/JavaScript/.
rm -rvf docs/_static
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/^([[:blank:]]*(black|zimports))\b/# &/' tox.ini
# Don't treat DeprecationWarnings as errors in tests
sed -i '/"error", category=DeprecationWarning/d' alembic/testing/warnings.py


%generate_buildrequires
%pyproject_buildrequires -x tz


%build
%pyproject_wheel

mkdir -p bin
echo '%{python3} -c "import alembic.config; alembic.config.main()" $*' > bin/alembic
chmod 0755 bin/alembic
help2man --version-string %{version} --no-info -s 1 bin/alembic > alembic.1


%install
install -d -m 0755 %{buildroot}%{_mandir}/man1

%pyproject_install
%pyproject_save_files alembic
mv %{buildroot}/%{_bindir}/alembic %{buildroot}/%{_bindir}/alembic-3
ln -s alembic-3 %{buildroot}/%{_bindir}/alembic-%{python3_version}
install -m 0644 alembic.1 %{buildroot}%{_mandir}/man1/alembic-3.1
ln -s alembic-3.1 %{buildroot}%{_mandir}/man1/alembic-%{python3_version}.1

ln -s alembic-%{python3_version} %{buildroot}/%{_bindir}/alembic
ln -s alembic-%{python3_version}.1 %{buildroot}%{_mandir}/man1/alembic.1


%check
%pytest %{?!rhel:-n auto}


%files -n python3-alembic -f %{pyproject_files}
# pyproject_files handles LICENSE; verify with rpm -qL -p ...
%doc README.rst CHANGES
%{_bindir}/alembic
%{_mandir}/man1/alembic.1{,.*}
%{_bindir}/alembic-3
%{_mandir}/man1/alembic-3.1{,.*}
%{_bindir}/alembic-%{python3_version}
%{_mandir}/man1/alembic-%{python3_version}.1{,.*}


%files -n python3-alembic+tz
%ghost %{python3_sitelib}/*.dist-info


%changelog
%autochangelog
