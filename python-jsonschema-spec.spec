%global srcname jsonschema-spec
%global modname jsonschema_spec

Name:           python-%{srcname}
Version:        0.1.6
Release:        %autorelease
Summary:        JSONSchema Spec with object-oriented paths

License:        Apache-2.0
URL:            https://github.com/p1c2u/%{srcname}
# The GitHub archive has the tests; the PyPI sdist does not.
Source:         %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Do not require quite such a recent version of requests
#
# Until python-requests is updated to 2.31.0[1], loosen the minimum version to
# 2.28.1. It is an optional dependency that was added with “deptry”
# analysis[2], which is only really useful for upstream CI, but it is also
# imported from jsonschema_spec/handlers/requests.py. There is no obvious
# reason why the most recent version (ahead of Rawhide as of this writing)
# should be needed.
#
# [1] https://bugzilla.redhat.com/show_bug.cgi?id=2189970
# [2] https://github.com/p1c2u/jsonschema-spec/commit/d207d233e31198942ba417875e2c1e09f848ab5d
Patch:          0001-Do-not-require-quite-such-a-recent-version-of-reques.patch

# Don't check with SupportsRead
# https://github.com/p1c2u/jsonschema-spec/pull/46
#
# Fixes:
#
# Test failures (regressions) with Python 3.12
# https://github.com/p1c2u/jsonschema-spec/issues/42
#
# F39FailsToInstall: python3-jsonschema-spec
# https://bugzilla.redhat.com/show_bug.cgi?id=2220292
#
# Backported to 0.1.6.
Patch:          0001-Don-t-check-with-SupportsRead.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
A python library which provides traverse JSON resources like paths and
access resources on demand with separate accessor layer.}

%description %_description


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -n %{srcname}-%{version} -p1
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i '/^--cov[-=]/d' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{modname}


%check
%pytest


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
%autochangelog
