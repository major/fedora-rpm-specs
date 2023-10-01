%if %{defined fedora}
%bcond_without ptipython
%endif

Name:           ptpython
Version:        3.0.23
Release:        %autorelease
Summary:        Python REPL build on top of prompt_toolkit
License:        BSD-3-Clause
URL:            https://github.com/prompt-toolkit/ptpython
Source:         %{pypi_source ptpython}
BuildArch:      noarch

%global common_description %{expand:
Ptpython is an advanced Python REPL built on top of the prompt_toolkit library.
It features syntax highlighting, multiline editing (the up arrow works),
autocompletion, mouse support, support for color schemes, support for bracketed
paste, both Vi and Emacs key bindings, support for double width (Chinese)
characters, and many other things.}


%description %{common_description}


%package -n ptpython3
Summary:        %{summary}
BuildRequires:  python3-devel
Provides:       ptpython = %{version}-%{release}
%py_provides    python3-ptpython


%description -n ptpython3 %{common_description}


%prep
%autosetup
find -name \*.py | xargs sed -i -e '1 {/^#!\//d}'


%generate_buildrequires
%pyproject_buildrequires %{?with_ptipython:-x ptipython}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files ptpython
%if %{without ptipython}
rm %{buildroot}%{_bindir}/ptipython*
%endif


%check
%pyproject_check_import -e ptpython.contrib.asyncssh_repl %{!?with_ptipython:-e ptpython.ipython}


%files -n ptpython3 -f %{pyproject_files}
%doc CHANGELOG README.rst
%{_bindir}/ptpython
%{_bindir}/ptpython3
%{_bindir}/ptpython%{python3_version}


%if %{with ptipython}
%pyproject_extras_subpkg -n ptpython3 ptipython
%{_bindir}/ptipython
%{_bindir}/ptipython3
%{_bindir}/ptipython%{python3_version}
%endif


%changelog
%autochangelog
