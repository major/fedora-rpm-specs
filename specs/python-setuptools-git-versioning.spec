# upstream tests require the upstream repo, so we can't run those

Name:       python-setuptools-git-versioning
Version:    2.1.0
Release:    %autorelease
Summary:    Use git repo data for building a version number according PEP-440

License:    MIT
URL:        https://setuptools-git-versioning.readthedocs.io/
Source0:    https://github.com/dolfinus/setuptools-git-versioning/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:  noarch


%global _description %{expand:
Use git repo data (latest tag, current commit hash, etc) for building a version
number according PEP 440.

Features:
- Can be installed & configured through both setup.py and PEP 518’s
  pyproject.toml
- Does not require to change source code of the project
- Tag-, file-, and callback-based versioning schemas are supported
- Templates for tag, dev and dirty versions are separated
- Templates support a lot of substitutions including git and environment
  information
- Well-documented

Limitations:
- Currently the only supported VCS is Git
- Only git v2 is supported
- Currently does not support automatic exporting of package version to a file
  for runtime use (but you can use setuptools-git-versioning > file redirect
  instead)
}

%description %_description

%package -n python3-setuptools-git-versioning
Summary:    Support for physical quantities with units, based on numpy
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
# man page
BuildRequires:  help2man

%description -n python3-setuptools-git-versioning %_description

%prep
%autosetup -n setuptools-git-versioning-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l setuptools_git_versioning

for binary in setuptools-git-versioning
do
    echo "Generating man page for ${binary// /-/}"
    PYTHONPATH="$PYTHONPATH:%{buildroot}/%{python3_sitelib}/" PATH="$PATH:%{buildroot}/%{_bindir}/" help2man --no-info --no-discard-stderr --name="${binary}" --version-string="${binary} %{version}" --output="${binary// /-}.1" "${binary}"
    cat "${binary// /-}.1"
    install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D "${binary// /-}.1"
done

%check
%pyproject_check_import

%files -n python3-setuptools-git-versioning -f %{pyproject_files}
%{_bindir}/setuptools-git-versioning
%{_mandir}/man1/setuptools-git-versioning.*

%changelog
%autochangelog
