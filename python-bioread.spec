Name:           python-bioread
Version:        3.0.1
Release:        %autorelease
Summary:        Utilities to read BIOPAC AcqKnowledge files

# SPDX
License:        MIT
URL:            https://github.com/uwmadison-chm/bioread
# The GitHub archive contains data required for running the tests, which the
# PyPI sdists lack.
Source:         %{url}/archive/v%{version}/bioread-%{version}.tar.gz

BuildArch:      noarch
 
BuildRequires:  python3-devel

# We could use the unittest module to run the tests, but pytest is more flexible.
BuildRequires:  %{py3_dist pytest}

BuildRequires:  help2man

%global common_description %{expand:
These utilities are for reading the files produced by BIOPAC’s AcqKnowledge
software. Much of the information is based on Application Note 156 from BIOPAC;
however, newer file formats were decoded through the tireless efforts of John
Ollinger and Nate Vack.

This library is mostly concerned with getting you the data, and less so with
interpreting UI-related header values.}

%description %{common_description}


%package -n     python3-bioread
Summary:        %{summary}

%description -n python3-bioread %{common_description}


%pyproject_extras_subpkg -n python3-bioread mat hdf5 all


%prep
%autosetup -n bioread-%{version}

# Upstream may like to run these as scripts during development, but they will
# be installed under site-packages without executable permissions, so we should
# remove the shebangs.
find bioread/runners/ -type f -name '*.py' -exec sed -r -i '1{/^#!/d}' '{}' '+'
# We might as well go ahead and drop the executable bit while we’re at it.
find bioread/runners/ -type f -perm /0111 -exec chmod -v a-x '{}' '+'


%generate_buildrequires
%pyproject_buildrequires -x all


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l bioread

# Do this in %%install rather than %%build because we need the entry points:
install -d '%{buildroot}%{_mandir}/man1'
for bin in acq2hdf5 acq2mat acq2txt acq_info acq_markers
do
  PYTHONPATH='%{buildroot}%{python3_sitelib}' help2man \
      --no-info \
      --version-string='%{version}' \
      --output="%{buildroot}%{_mandir}/man1/${bin}.1" \
      "%{buildroot}%{_bindir}/${bin}"
done


%check
%pytest -k "${k-}" -v


%files -n python3-bioread -f %{pyproject_files}
%doc README.md
%doc examples/

%{_bindir}/acq2hdf5
%{_bindir}/acq2mat
%{_bindir}/acq2txt
%{_bindir}/acq_info
%{_bindir}/acq_markers

%{_mandir}/man1/acq2hdf5.1*
%{_mandir}/man1/acq2mat.1*
%{_mandir}/man1/acq2txt.1*
%{_mandir}/man1/acq_info.1*
%{_mandir}/man1/acq_markers.1*


%changelog
%autochangelog
