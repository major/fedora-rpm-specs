
Name:           python-markdown-include
Version:        0.6.0
Release:        %autorelease
Summary:        Syntax for Python-Markdown to include other Markdown documents

License:        GPLv3
URL:            https://github.com/cmacmackin/markdown-include
# We use the GitHub tarball because the PyPI archive is missing LICENSE.txt.
Source0:        %{url}/archive/v%{version}/markdown-include-%{version}.tar.gz
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
# Remove shebang line in non-script source
sed -r -i '1{/^#!/d}' markdown_include/include.py


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files markdown_include


%check
# There are no tests.
%pyproject_check_import


%files -n python3-markdown-include -f %{pyproject_files}
%doc README.*


%changelog
%autochangelog
