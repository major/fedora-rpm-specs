# Remove -s from Python shebang - ensure that extensions installed with pip
# to user locations are seen and properly loaded
%undefine _py3_shebang_s

%global forgeurl https://github.com/PyCQA/pylint
%global basever 4.0.2
#%%global prever b0
Version:        4.0.2
%forgemeta

Name:           pylint
Release:        %autorelease
Summary:        Analyzes Python code looking for bugs and signs of poor quality
License:        GPL-2.0-or-later
URL:            https://github.com/pylint-dev/pylint
Source0:        %{forgeurl}/archive/v%{basever}/pylint-%{basever}.tar.gz
#Patch0:         7829.patch apply when rebased then re-enable tests
Patch1:         pep639.patch
BuildArch:      noarch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
# For tests
BuildRequires:  python3-GitPython
BuildRequires:  python3-pytest-benchmark
BuildRequires:  python3-pytest-xdist
BuildRequires:  python3-typing-extensions
BuildRequires:  graphviz

# For the main pylint package
Requires:       python3-%{name} = %{version}-%{release}

%global _description %{expand:
Pylint is a Python source code analyzer which looks for programming errors,
helps enforcing a coding standard and sniffs for some code smells (as defined in
Martin Fowler's Refactoring book). Pylint can be seen as another PyChecker since
nearly all tests you can do with PyChecker can also be done with Pylint.
However, Pylint offers some more features, like checking length of lines of
code, checking if variable names are well-formed according to your coding
standard, or checking if declared interfaces are truly implemented, and much
more.

Additionally, it is possible to write plugins to add your own checks.}

%description %_description

%package -n python3-%{name}
Summary:        %{summary}

%description -n python3-%{name} %_description

%prep
%autosetup -p1 -n %{name}-%{basever}
# Relax version requirements
sed -i -e 's/"setuptools>=[^"]*"/"setuptools"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
rm -rf %{buildroot}%{python3_sitelib}/pylint/test

# Add -%%{python3_version} to the binaries and manpages for backwards compatibility
for NAME in pylint pyreverse symilar; do
    mv %{buildroot}%{_bindir}/{$NAME,${NAME}-%{python3_version}}
    ln -s ${NAME}-%{python3_version} %{buildroot}%{_bindir}/${NAME}-3
    ln -s ${NAME}-%{python3_version} %{buildroot}%{_bindir}/${NAME}
done

%check
# Skip benchmarks
# Deselect all tests failing with Python 3.14
%pytest -v --ignore=benchmark \
  -n auto \
  --deselect=tests/test_functional.py::test_functional[missing_timeout] \
  --deselect=tests/config/pylint_config/test_pylint_config_help.py::test_pylint_config_main_messages \
  --deselect=tests/pyreverse/test_writer.py::test_dot_files[packages_No_Name.dot] \
  --deselect=tests/pyreverse/test_writer.py::test_dot_files[classes_No_Name.dot] \
  --deselect=tests/pyreverse/test_writer.py::test_colorized_dot_files[packages_colorized.dot] \
  --deselect=tests/pyreverse/test_writer.py::test_colorized_dot_files[classes_colorized.dot] \
  --deselect=tests/pyreverse/test_writer.py::test_no_standalone_dot_files[classes_no_standalone.dot] \
  --deselect=tests/pyreverse/test_writer.py::test_no_standalone_dot_files[packages_no_standalone.dot] \
  --deselect=tests/pyreverse/test_writer.py::test_type_check_imports_dot_files[packages_type_check_imports.dot] \
  --deselect=tests/pyreverse/test_writer.py::test_type_check_imports_dot_files[classes_type_check_imports.dot] \
  --deselect=tests/pyreverse/test_writer.py::test_puml_files[packages_No_Name.puml] \
  --deselect=tests/pyreverse/test_writer.py::test_puml_files[classes_No_Name.puml] \
  --deselect=tests/pyreverse/test_writer.py::test_mmd_files[packages_No_Name.mmd] \
  --deselect=tests/pyreverse/test_writer.py::test_mmd_files[classes_No_Name.mmd] \
  --deselect=tests/pyreverse/test_writer.py::test_html_files[packages_No_Name.html] \
  --deselect=tests/pyreverse/test_writer.py::test_html_files[classes_No_Name.html] \
  --deselect=tests/pyreverse/test_writer.py::test_colorized_puml_files[packages_colorized.puml] \
  --deselect=tests/pyreverse/test_writer.py::test_colorized_puml_files[classes_colorized.puml] \
  --deselect=tests/test_functional.py::test_functional[continue_in_finally] \
  --deselect=tests/test_functional.py::test_functional[consider_using_with] \
  --deselect=tests/test_functional.py::test_functional[typing_broken_callable] \
  --deselect=tests/test_functional.py::test_functional[typing_broken_callable_future_import] \
  --deselect=tests/test_functional.py::test_functional[typing_consider_using_union] \
  --deselect=tests/test_functional.py::test_functional[typing_consider_using_union_py310] \
  --deselect=tests/test_functional.py::test_functional[typing_consider_using_union_without_future] \
  --deselect=tests/test_functional.py::test_functional[function_redefined_2540] \
  --deselect=tests/test_functional.py::test_functional[generic_alias_collections] \
  --deselect=tests/test_functional.py::test_functional[generic_alias_mixed_py39] \
  --deselect=tests/test_functional.py::test_functional[generic_alias_typing] \
  --deselect=tests/test_functional.py::test_functional[lost_exception] \
  --deselect=tests/test_functional.py::test_functional[return_in_finally] \
  --deselect=tests/test_functional.py::test_functional[wrong_import_order] \
  --deselect=tests/test_import_graph.py::test_dependencies_graph[foo.dot] \
  --deselect=tests/test_import_graph.py::test_dependencies_graph[foo.gv] \
  --deselect=tests/test_import_graph.py::test_dependencies_graph[tests/regrtest_data/foo.dot] \
  --deselect=tests/test_import_graph.py::test_checker_dep_graphs \
  --deselect=tests/test_self.py::TestRunTC::test_do_not_import_files_from_local_directory[args0] \
  --deselect=tests/test_self.py::TestRunTC::test_do_not_import_files_from_local_directory[args1] \
  --deselect=tests/test_self.py::TestRunTC::test_progress_reporting \
  --deselect=tests/pyreverse/test_diadefs.py::TestDefaultDiadefGenerator::test_functional_relation_extraction

%files
%doc CONTRIBUTORS.txt
%license LICENSE
%{_bindir}/pylint
%{_bindir}/pylint-config
%{_bindir}/pyreverse
%{_bindir}/symilar

%files -n python3-%{name}
%license LICENSE
%{python3_sitelib}/pylint*
# backwards compatible versioned executables and manpages:
%{_bindir}/*-3
%{_bindir}/*-%{python3_version}

%changelog
%autochangelog
