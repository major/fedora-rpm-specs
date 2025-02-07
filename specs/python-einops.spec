%global pypi_name einops
%global pypi_version 0.8.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        %autorelease
Summary:        Deep learning operations reinvented

License:        MIT
URL:            https://github.com/arogozhnikov/einops
Source0:        %{url}/archive/v%{version}.tar.gz#/%{pypi_name}-%{pypi_version}.tar.gz

BuildArch:      noarch
# Pytorch only on X86_64 and aarch64
ExclusiveArch:  x86_64 aarch64

BuildRequires:  python3-devel
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(nbformat)
BuildRequires:  python3dist(nbconvert)
BuildRequires:  python3dist(parameterized)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(torch)

# For test
BuildRequires:  jupyterlab
BuildRequires:  python3dist(notebook)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(ipython)
BuildRequires:  python3dist(ipywidgets)
BuildRequires:  python3dist(ipykernel)
BuildRequires:  python3dist(jupyter-console)

%description
Flexible and powerful tensor operations for readable and reliable code.
Supports numpy, pytorch, tensorflow, jax, and others.

%package -n     python3-%{pypi_name}
Summary:        Deep learning operations reinvented

%description -n python3-%{pypi_name}
Flexible and powerful tensor operations for readable and reliable code.
Supports numpy, pytorch, tensorflow, jax, and others.

%prep
%autosetup -n %{pypi_name}-%{pypi_version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# To prevent import errors, remove the frameworks we have no support for.
rm einops/layers/chainer.py
rm einops/layers/flax.py
rm einops/layers/keras.py
rm einops/layers/oneflow.py
rm einops/layers/paddle.py
rm einops/layers/tensorflow.py

# numpy 2
# import numpy.array_api as -> import numpy as
# Fixed in the upstream with
# commit 11680b457ce2216d9827330d0b794565946847d7
# Author: Alex Rogozhnikov <iamfullofspam@gmail.com>
# Date:   Wed Aug 7 17:35:43 2024 -0700
#
#    fix tests for numpy regression (see https://github.com/numpy/numpy/issues/27137)
#
sed -i -e 's@import numpy.array_api as@import numpy as@' tests/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import
export PYTHONPATH=$PYTHONPATH:%{buildroot}%{python3_sitelib}/%{pypi_name}
# AttributeError: 'numpy.int64' object has no attribute '__dlpack__'
k="${k-}${k+ and }not (test_ops and test_reduce_array_api)"
# ImportError: attempted relative import with no known parent package
k="${k-}${k+ and }not (test_notebooks and test_notebook_1)"
k="${k-}${k+ and }not (test_notebooks and test_notebook_2_with_all_backends)"
k="${k-}${k+ and }not (test_notebooks and test_notebook_3)"
k="${k-}${k+ and }not (test_notebooks and test_notebook_4)"
# RuntimeError: Dynamo is not supported on Python 3.13+
k="${k-}${k+ and }not (test_other and test_torch_compile)"
k="${k-}${k+ and }not (test_ops and test_torch_compile_with_dynamic_shape)"
EINOPS_TEST_BACKENDS=numpy %pytest -k "${k-}" tests
EINOPS_TEST_BACKENDS=torch %pytest -k "${k-}" tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
