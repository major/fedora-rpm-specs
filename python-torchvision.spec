%global pypi_name torchvision
%global pypi_version 0.16.0

%bcond_with gitcommit
%if %{with gitcommit}
# The top of the 0.16 branch - update to whatever..
%global commit0 fbb4cc54ed521ba912f50f180dc16a213775bf5c
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%endif

# check takes too long, make optional
%bcond_with test

# torch toolchain
%global toolchain clang

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        6%{?dist}
Summary:        Image and video datasets for torch deep learning

License:        BSD-3-Clause AND BSD-2-Clause AND MIT
URL:            https://github.com/pytorch/vision
%if %{with gitcommit}
Source0:        %{url}/archive/%{commit0}/vision-%{shortcommit0}.tar.gz
%else
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/vision-v%{version}.tar.gz
# Need at least -g debugging
# Find where ffmpeg header and libs are
Patch0:         0001-prepare-python-torchvision-setup-for-fedora.patch
# https://github.com/pytorch/vision/pull/8096/commits/86620bd84b872b76db0acafec167949dca03a29e
Patch1:         0001-AV_CODEC_CAP_INTRA_ONLY-is-not-defined.patch
# Do not import models
Patch2:         0001-Remove-models-from-torchvision.patch
%endif

# Limit to these because that is what torch is on
ExclusiveArch:  x86_64 aarch64

BuildRequires:  clang
BuildRequires:  ffmpeg-free
BuildRequires:  ffmpeg-free-devel
BuildRequires:  libavcodec-free-devel
BuildRequires:  libavformat-free-devel
BuildRequires:  libavutil-free-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libswresample-free-devel
BuildRequires:  libswscale-free-devel
BuildRequires:  ninja-build
BuildRequires:  python3-devel
BuildRequires:  python3-torch-devel
BuildRequires:  zlib-devel

BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(setuptools)

%if %{with test}
BuildRequires: python3dist(pytest)
%endif

Requires:      python3dist(numpy)
Requires:      python3dist(pillow)
Requires:      python3dist(requests)
Requires:      python3dist(torch)

%description
The torchvision package consists of popular datasets, model architectures,
and common image transformations for computer vision.

%package -n     python3-%{pypi_name}
Summary:        Image and video datasets for torch deep learning

%description -n python3-%{pypi_name}
The torchvision package consists of popular datasets, model architectures,
and common image transformations for computer vision.

%prep
%if %{with gitcommit}
%autosetup -p1 -n vision-%{commit0}
%else
%autosetup -p1 -n vision-%{version}
%endif

# Remove pretrained models
# https://github.com/pytorch/vision/issues/2597
# If we are testing, include the models.
%if %{without test}
rm -rf torchvision/models
%endif

%generate_buildrequires
%pyproject_buildrequires -t

%build
# Building uses python3_sitearch/torch/utils/cpp_extension.py
# cpp_extension.py does a general linking with all the pytorch libs which
# leads warnings being reported by rpmlint.
%pyproject_wheel

%if %{with test}
%check
%pytest
%endif

%install
%pyproject_install

# exec permission
for f in `find %{buildroot}%{python3_sitearch} -name '*.py'`; do
    if [ ! -x $f ]; then
        sed -i '1{\@^#!/usr/bin@d}' $f
    fi
done

%files -n python3-%{pypi_name}

%license LICENSE
%doc README.md 
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{pypi_version}.dist-info

# License details
# From license check output
#
# *No copyright* Creative Commons Attribution-NonCommercial 4.0
# -------------------------------------------------------------
# vision-0.16.0/README.md
# 
# - from this section of README.md
#
## Pre-trained Model License
#
# The pre-trained models provided in this library may have their own licenses or terms and conditions derived from the
# dataset used for training. It is your responsibility to determine whether you have permission to use the models for your
# use case.
# 
# More specifically, SWAG models are released under the CC-BY-NC 4.0 license. See
# [SWAG LICENSE](https://github.com/facebookresearch/SWAG/blob/main/LICENSE) for additional details.
#
# - this has been remediated by removing the the torchvision/models/ dir in prep

%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 16 2023 Tom Rix <trix@redhat.com> - 0.16.0-5
- Remove pretrained models
- Remove autogeneration of dirs

* Mon Dec 4 2023 Tom Rix <trix@redhat.com> - 0.16.0-4
- Use python-torch
- enable jpeg, png, ffmpeg
- Fix exec permission

* Sat Oct 14 2023 Tom Rix <trix@redhat.com> - 0.16.0-3
- Convert to pyproject_ 

* Tue Oct 10 2023 Tom Rix <trix@redhat.com> - 0.16.0-2
- Use released 0.16.0

* Sat Sep 30 2023 Tom Rix <trix@redhat.com> - 0.16.0-1
- Initial package.


