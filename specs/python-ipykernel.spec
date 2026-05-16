# When we bootstrap new Python, we need to avoid a build dependency loop
%bcond bootstrap 0
%bcond tests %{without bootstrap}

Name:           python-ipykernel
Version:        7.2.0
Release:        %autorelease
Summary:        IPython Kernel for Jupyter
License:        BSD-3-Clause
URL:            https://github.com/ipython/ipykernel
Source:         https://github.com/ipython/ipykernel/releases/download/v%{version}/ipykernel-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description \
This package provides the IPython kernel for Jupyter.

%description %{_description}


%package -n python3-ipykernel
Summary:        %{summary}
Requires:       python-jupyter-filesystem

# We removed the -doc subpackage for Fedora 42.
Obsoletes:      python-ipykernel-doc < 6.29.3-8

%description -n python3-ipykernel %{_description}

%prep
%autosetup -p1 -n ipykernel-%{version}

# Remove the dependency on debugpy.
# See https://github.com/ipython/ipykernel/pull/767
%pyproject_patch_dependency debugpy:ignore

# Remove test dependencies on pre-commit (used for linting) and pytest-cov; see
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters.
%pyproject_patch_dependency pre-commit:ignore
%pyproject_patch_dependency pytest-cov:ignore
sed -i 's/request.config.getvalue("--cov")/False/' tests/test_subshells.py


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x test}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l ipykernel ipykernel_launcher

# Install the kernel so it can be found
# See https://bugzilla.redhat.com/show_bug.cgi?id=1327979#c19
%{python3} -m ipykernel install --prefix %{buildroot}%{_prefix}
ls %{buildroot}%{_datadir}/jupyter/kernels/python3/
cat %{buildroot}%{_datadir}/jupyter/kernels/python3/kernel.json


%check
%if %{with tests}
%pytest -Wdefault
%else
# datapub, pickleutil, serialize need ipyparallel
# pylab needs matplotlib
# trio needs trio
# debugger needs debugpy
# gui needs gobject
%{pyproject_check_import \
    -e ipykernel.datapub -e ipykernel.pickleutil -e ipykernel.serialize \
    -e 'ipykernel.pylab*' \
    -e 'ipykernel.trio*' \
    -e ipykernel.debugger \
    -e 'ipykernel.gui*' \
    -e '*.test*'}
%endif


%files -n python3-ipykernel -f %{pyproject_files}
%doc CONTRIBUTING.md README.md
%{_datadir}/jupyter/kernels/python3


%changelog
%autochangelog
