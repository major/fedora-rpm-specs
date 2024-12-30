Name:           python-huggingface-hub
Version:        0.27.0
Release:        %autorelease
Summary:        Client library to handle repos on the huggingface.co hub

License:        Apache-2.0
URL:            https://github.com/huggingface/huggingface_hub
Source:         %{pypi_source huggingface_hub}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
The huggingface_hub library allows you to interact with the Hugging Face Hub, a
machine learning platform for creators and collaborators. Discover pre-trained
models and datasets for your projects or play with the hundreds of machine
learning apps hosted on the Hub. You can also create and share your own models
and datasets with the community. The huggingface_hub library provides a simple
way to do all these things with Python.
}

%description %_description

%package -n     python3-huggingface-hub
Summary:        %{summary}

%description -n python3-huggingface-hub %_description

# if you are missing somewhere and the dependencies are in fedora, let me know to enable it
# leaving it here as a comment so I know later how to enable it
#%%pyproject_extras_subpkg -n python3-huggingface-hub cli,,fastai,hf-transfer,inference,quality,tensorflow,tensorflow-testing,testing,torch,typing


%prep
%autosetup -p1 -n huggingface_hub-%{version}


%generate_buildrequires
# available extras
# if you are missing somewhere and the dependencies are in fedora, let me know to enable it
# cli,fastai,hf-transfer,inference,quality,tensorflow,tensorflow-testing,testing,typing
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files 'huggingface_hub'


%check
# PyPI tar ball does not include tests
# checking just import is enough for now
%pyproject_check_import


%files -n python3-huggingface-hub -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/huggingface-cli

%changelog
%autochangelog
