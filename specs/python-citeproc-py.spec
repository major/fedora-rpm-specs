Name:           python-citeproc-py
Version:        0.7.0
Release:        %autorelease
Summary:        Citations and bibliography formatter

License:        BSD-2-Clause
URL:            https://github.com/citeproc-py/citeproc-py
# upstream forgot to release on GitHub, so we use pypi_source for the moment
Source0:        %{pypi_source citeproc_py}

BuildArch:      noarch

%description
%{summary}.

%package -n python3-citeproc-py
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

%description -n python3-citeproc-py
%{summary}.

%prep
%autosetup -n citeproc_py-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

sed -i -e '1s|^.*$|#!%{__python3}|' %{buildroot}%{_bindir}/csl_unsorted

%pyproject_save_files -l citeproc

%check
%{pytest}


%files -n python3-citeproc-py -f %{pyproject_files}
%{_bindir}/csl_unsorted

%changelog
%autochangelog
