%global _description %{expand:
After 10 years juggling with os.path, zipfile & Co. I thought it is time to
bring back more pythonic to APIs. It is made with the philosophy that API's
should be intuitive and their defaults should at least cover 80% of what
programmer daily needs. Started with the semantic file system pathes, it grows
continuous and includes more and more handy stuff for the daily python
scripting.}

Name:           python-fspath
Version:        20230629
Release:        %{autorelease}
Summary:        Handling path names and executables more comfortable


License:        AGPL-3.0-or-later
URL:            http://return42.github.io/fspath
Source:         %{pypi_source fspath}

BuildArch:      noarch

%description %_description

%package -n python3-fspath
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n python3-fspath %_description

%prep
%autosetup -n fspath-%{version}

# remove shebangs
for f in fspath/{cli,debug,os_env}.py
do
    sed -i '1d' "$f"
done

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l fspath

%check
# tries to download the zip and then do stuff on the zip
export TEST_TEMPDIR=$RPM_BUILD_ROOT/%{_tmppath}
%pytest tests -k "not test_download and not test_ZIP"

%files -n python3-fspath -f %{pyproject_files}
%doc README.rst
%{_bindir}/fspath
%{_bindir}/which.py

%changelog
%autochangelog
