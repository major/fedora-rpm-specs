%global srcname tree-sitter
%global modname tree_sitter

Name:           python-%{srcname}
Version:        0.26.1
Release:        %autorelease
Summary:        Python bindings to the Tree-sitter parsing library
License:        MIT
URL:            https://github.com/tree-sitter/py-tree-sitter
Source0:        %{url}/archive/v%{version}/py-tree-sitter-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libtree-sitter-devel
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
Python bindings to the Tree-sitter parsing library. Tree-sitter is a parser
generator tool and an incremental parsing library. It can build a concrete
syntax tree for a source file and efficiently update the syntax tree as the
source file is edited.}

%description %_description


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -p1 -n py-%{srcname}-%{version}

# Use system libtree-sitter instead of the bundled submodule
sed -i setup.py \
    -e '/tree_sitter\/core\/lib\/src\/lib.c/d' \
    -e '/tree_sitter\/core\/lib\/include/d' \
    -e '/tree_sitter\/core\/lib\/src/d' \
    -e '/define_macros=\[/i\        libraries=["tree-sitter"],'


%generate_buildrequires
%pyproject_buildrequires -x tests


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{modname}


%check
%pyproject_check_import
%{py3_test_envvars} %{python3} -P -m unittest discover -s tests -v


%files -n python3-%{srcname} -f %{pyproject_files}


%changelog
%autochangelog
