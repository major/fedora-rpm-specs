Name:           python-pari-jupyter
Version:        1.4.3
Release:        %autorelease
Summary:        Jupyter kernel for PARI/GP

License:        GPL-3.0-or-later
URL:            https://github.com/sagemath/pari-jupyter
VCS:            git:%{url}.git
Source:         %{url}/archive/%{version}/pari-jupyter-%{version}.tar.gz
# Adapt to recent versions of pari
Patch:          %{name}-pari.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    pyproject
BuildOption(install): -l PARIKernel

BuildRequires:  gcc
BuildRequires:  pari-devel
BuildRequires:  pari-gp
BuildRequires:  pkgconfig(readline)
BuildRequires:  %{py3_dist cython}
BuildRequires:  %{py3_dist docutils}
BuildRequires:  %{py3_dist jupyter_kernel_test}

%description
This package contains a Jupyter kernel for PARI/GP.

%package     -n python3-pari-jupyter
Summary:        Jupyter kernel for PARI/GP
Requires:       pari-gp
Requires:       python-jupyter-filesystem

%py_provides python3-PARIKernel

%description -n python3-pari-jupyter
This package contains a Jupyter kernel for PARI/GP.

%prep
%autosetup -n pari-jupyter-%{version} -p1

%build -a
rst2html --no-datestamp README.rst README.html

%install -a
# Move the config file to the right place
mkdir -p %{buildroot}%{_sysconfdir}/jupyter/nbconfig
mv %{buildroot}%{_prefix}%{_sysconfdir}/jupyter/nbconfig/notebook.d \
   %{buildroot}%{_sysconfdir}/jupyter/nbconfig
rm -fr %{buildroot}%{_prefix}%{_sysconfdir}

%check
export IPYTHONDIR=$PWD/.ipython
mkdir .ipython
ln -s %{buildroot}%{_datadir}/jupyter/kernels .ipython
ln -s %{buildroot}%{_datadir}/jupyter/nbextensions .ipython
cd test
%{py3_test_envvars} %{python3} test_pari_jupyter_kernel.py
cd -
rm -fr .ipython

%files -n python3-pari-jupyter -f %{pyproject_files}
%doc README.html
%config(noreplace) %{_sysconfdir}/jupyter/nbconfig/notebook.d/gp-mode.json
%{_datadir}/jupyter/kernels/pari_jupyter/
%{_datadir}/jupyter/nbextensions/gp-mode/

%changelog
%autochangelog
