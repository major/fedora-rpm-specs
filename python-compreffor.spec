Name:           python-compreffor
Version:        0.5.5
Release:        %autorelease
Summary:        CFF table subroutinizer for FontTools

License:        Apache-2.0
URL:            https://github.com/googlefonts/compreffor
Source0:        %{url}/archive/%{version}/compreffor-%{version}.tar.gz
# Man page written by hand for Fedora in groff_man(7) format using the
# command’s --help output
Source1:        compreffor.1

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel

BuildRequires:  make
BuildRequires:  gcc-c++
# From setup.py: cython_min_version = '0.29.24'
BuildRequires:  python3dist(cython) >= 0.29.24

%global common_description %{expand:
A CFF (Compact Font Format) table subroutinizer for FontTools.}

%description %{common_description}


%package -n python3-compreffor
Summary:        %{summary}

%description -n python3-compreffor %{common_description}


%prep
%autosetup -n compreffor-%{version}

# Drop the setuptools_git_ls_files dependency
#
# This dependency makes sense upstream, but we do not need it (and it is
# not packaged) in Fedora.
sed -r -i '/setuptools_git_ls_files/d' pyproject.toml
sed -r -i 's/, "setuptools_git_ls_files"//' setup.py

# Remove shebangs from non-script sources. The find-then-modify pattern
# preserves mtimes on sources that did not need to be modified.
find 'src' -type f -name '*.py' \
    -exec gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r sed -r -i '1{/^#!/d}'

# Remove Cython-generated sources; we must ensure they are regenerated.
find src/cython -type f -name '*.c*' -print -delete

# Do not use requirements.txt for tox dependencies, as it contains (only) an
# overly-strict pinned fonttools version.
sed -r -i '/^[[:blank:]]*-rrequirements.txt[[:blank:]]*/d' 'tox.ini'


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires -t


%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l compreffor
install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D '%{SOURCE1}'


%check
%tox


%files -n python3-compreffor -f %{pyproject_files}
%doc README.rst

%{_bindir}/compreffor
%{_mandir}/man1/compreffor.1*


%changelog
%autochangelog
