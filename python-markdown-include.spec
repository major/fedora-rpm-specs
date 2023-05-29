Name:           python-markdown-include
Version:        0.8.1
Release:        %autorelease
Summary:        A Python-Markdown extension which provides an 'include' function

# The overall license is GPL-3.0-only, based on the trove classifier “License
# :: OSI Approved :: GNU General Public License v3 (GPLv3)” in setup.py and on
# the contents of LICENSE.txt. However, the primary source file
# markdown_include/include.py is clearly GPL-2.0-or-later based on its comment
# header.
License:        GPL-3.0-only AND GPL-2.0-or-later
URL:            https://github.com/cmacmackin/markdown-include
Source:         %{pypi_source markdown-include}

BuildArch:      noarch

BuildRequires:  python3-devel

%global common_description %{expand:
This is an extension to Python-Markdown which provides an “include” function,
similar to that found in LaTeX (and also the C pre-processor and Fortran). It
was originally written for the FORD Fortran auto-documentation generator.}

%description %{common_description}


%package -n     python3-markdown-include
Summary:        %{summary}

%description -n python3-markdown-include %{common_description}


%prep
%autosetup -n markdown-include-%{version}


%generate_buildrequires
%pyproject_buildrequires -x tests


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files markdown_include


%check
%pytest


%files -n python3-markdown-include -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
