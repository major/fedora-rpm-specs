%global         srcname     msal-extensions
%global         forgeurl    https://github.com/AzureAD/microsoft-authentication-extensions-for-python/
Version:        1.2.0
%global         tag         %{version}
%forgemeta

# We have generally figured out the dependencies for the libsecret tests, but
# they still hang in the test environment, so they remain disabled for now.
# We retain the work we have done so far in the spec file in case someone
# figures out what’s still missing to run these tests.
%bcond libsecret_tests 0

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Microsoft Authentication extensions for MSAL Python
License:        MIT
URL:            %forgeurl
Source:         %forgesource

# Downstream-only: restore hard dependency on pygobject
#
# Upstream omitted this dependency because they were not confident they could
# successfully "pip install" it, but we have no such difficulty with system
# packages. It is a real dependency for msal_extensions/libsecret.py.
Patch:          0001-Downstream-only-restore-hard-dependency-on-pygobject.patch
# Allow portalocker version 3
# https://github.com/AzureAD/microsoft-authentication-extensions-for-python/pull/136
# Rebased on top of 0001-Downstream-only-restore-hard-dependency-on-pygobject.patch.
Patch:          0002-Allow-portalocker-version-3.patch
# Fix a typo in README.md (persistance/persistence)
# https://github.com/AzureAD/microsoft-authentication-extensions-for-python/pull/133
Patch:          %{forgeurl}/pull/133.patch

BuildArch:      noarch

BuildRequires:  python3-devel
# Test runner; see tox.ini, but running tests via tox offers us no benefit:
BuildRequires:  %{py3_dist pytest}
%if %{with libsecret_tests}
# All of the following are needed for tests involving libsecret. We choose not
# to add a runtime dependency on libsecret because we expect that if we are
# running in a desktop session where it would be usable, it will be installed,
# and if it is not installed, it would not have been usable anyway (e.g.
# because the OS installation is "headless").
BuildRequires:  dbus-x11
BuildRequires:  gnome-keyring
BuildRequires:  libsecret
BuildRequires:  xorg-x11-server-Xvfb
%endif

%global _description %{expand:
The Microsoft Authentication Extensions for Python offers secure mechanisms for
client applications to perform cross-platform token cache serialization and
persistence. It gives additional support to the Microsoft Authentication Library
for Python (MSAL).

MSAL Python supports an in-memory cache by default and provides the
SerializableTokenCache to perform cache serialization. You can read more about
this in the MSAL Python documentation. Developers are required to implement
their own cache persistence across multiple platforms and Microsoft
Authentication Extensions makes this simpler.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%forgeautosetup -p1

# Remove DOS line endings
sed "s|\r||g" README.md >README.md.new && \
touch -r README.md README.md.new && \
mv README.md.new README.md


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l msal_extensions


%check
%if %{with libsecret_tests}
%global __pytest /usr/bin/xvfb-run -a pytest
%else
k="${k-}${k+ and }not test_libsecret_persistence"
k="${k-}${k+ and }not test_nonexistent_libsecret_persistence"
k="${k-}${k+ and }not test_token_cache_roundtrip_with_persistence_builder"
%endif
%pytest -k "${k-}" -v


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
