%global         pypi_name       tinygrad
%global         forgeurl        https://github.com/tinygrad/tinygrad
Version:        0.7.0
%forgemeta

Name:           python-%{pypi_name}
Release:        6%{?dist}
Summary:        You like pytorch? You like micrograd? You love tinygrad! 

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  python3-devel
# Needed for test
BuildRequires:  python3dist(pytest)
BuildArch: noarch

%global common_description %{expand:
tinygrad: For something between PyTorch and karpathy/micrograd. Maintained
by tiny corp.

This may not be the best deep learning framework, but it is a deep learning
framework.

Due to its extreme simplicity, it aims to be the easiest framework to add new
accelerators to, with support for both inference and training. If XLA is CISC,
tinygrad is RISC.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pypi_name}


%check
# Run CPU tests that do not need dependencies not in Fedora
# Modified from
# https://github.com/tinygrad/tinygrad/blob/master/.github/workflows/test.yml
%python3 -m pytest test/test_allocators.py \
                   test/test_assign.py \
                   test/test_conv.py \
                   test/test_conv_shapetracker.py \
                   test/test_gc.py \
                   test/test_helpers.py \
                   test/test_jit.py \
                   test/test_lazybuffer.py \
                   test/test_linearizer.py \
                   test/test_specific_conv.py \
                   test/test_symbolic_jit.py \
                   test/test_symbolic_ops.py \
                   test/test_symbolic_shapetracker.py \
                   test/test_uops.py

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc docs/quickstart.md
%doc docs/env_vars.md
%doc docs/abstractions.py


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Python Maint <python-maint@redhat.com> - 0.7.0-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 02 2023 Benson Muite <benson_muite@emailplus.org> - 0.7.0-1
- Initial package
