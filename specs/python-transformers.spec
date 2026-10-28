%global pypi_name transformers
# Has an error around _cuda_version that needs further digging
# Also has a circular dep
%define with_tests 0

Name:          python-transformers
Version:       5.21
Release:       1%{?dist}
Summary:       State-of-the-art Machine Learning for Pytorch, TensorFlow, and JAX
License:       Apache-2.0
URL:           https://github.com/huggingface/transformers
Source0:       %url/archive/v%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools
# For check
%if 0%{?with_tests}
BuildRequires: python3-pytest
BuildRequires: python3-huggingface-hub
BuildRequires: python3-ipython
BuildRequires: python3-pillow
BuildRequires: python3-requests
BuildRequires: python3-sentencepiece
BuildRequires: python3-torch
BuildRequires: python3-torchaudio
BuildRequires: python3-torchvision
BuildRequires: python3-transformers
%endif

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description
Source for python3-%{pypi_name}

%description -n python3-%{pypi_name}
Transformers provides thousands of pretrained models to perform tasks on
different modalities such as text, vision, and audio.

These models can be applied on:
• Text, for tasks like text classification, information extraction, question
answering, summarization, translation, text generation, in over 100 languages.
• Images, tasks like image classification, object detection, and segmentation.
• Audio, for tasks like speech recognition and audio classification.

Transformers provides APIs to quickly download and use those pretrained models
on a given text, fine-tune them on your own datasets and then share them with
the community on our model hub. At the same time, each python module defining
an architecture is fully standalone and can be modified to enable quick
research experiments.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%if 0%{?with_tests}
%pyproject_buildrequires -r
%else
%pyproject_buildrequires
%endif

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l %{pypi_name}

%if 0%{?with_tests}
%check
%pyproject_check_import
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%{_bindir}/transformers

%changelog
* Mon Oct 26 2026 Peter Robinson <pbrobinson@fedoraproject.org> - 5.21-1
- Initial package
