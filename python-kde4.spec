%define srcname pykde4

Name:python-kde4
Summary: KDE bindings to non-C++ languages
Version: 4.8.2
Release: 1
Epoch: 1
Group: Graphical desktop/KDE
License: GPLv2
URL: http://www.kde.org
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%srcname-%version.tar.xz
BuildRequires: kdepimlibs4-devel 
BuildRequires: python-sip >= 1:4.12
BuildRequires: python-qt4-devel >= 4.8.2
BuildRequires: automoc4
Group: Development/KDE and Qt
Provides: PyKDE4 = %epoch:%version-%release
Provides: pykde4 = %epoch:%version-%release
Requires: python-qt4 >= 4.8.2

%description
The Python bindings for KDE 4.

%files
%py_platsitedir/PyQt4/
%py_platsitedir/PyKDE4
%_kde_bindir/pykdeuic4
%_kde_libdir/kde4/kpythonpluginfactory.so
%dir %_kde_appsdir/pykde4
%exclude %_kde_datadir/doc/python-kde4

#-----------------------------------------------------------------------------

%package devel
Summary: PyKDE4 sip files and examples
Group: Development/KDE and Qt
Conflicts: python-kde4 < 1:4.5.77-0.svn1198704.2
Requires: python-kde4 = %epoch:%version-%release
Requires: python-qt4-devel

%description devel
Python KDE 4 sip files and examples.

%files devel
%_kde_datadir/sip/PyKDE4
%_kde_appsdir/pykde4/examples

#-----------------------------------------------------------------------------

%package doc
Summary: PyKDE4 documentation
Group: Development/KDE and Qt
BuildArch: noarch

%description doc
Python bindings for KDE 4 documentation.

%files doc
%doc AUTHORS COPYING COPYING.LESSER NEWS README THANKS
%_kde_datadir/doc/python-kde4

#------------------------------------------------------------

%prep
%setup -q -n %srcname-%version

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

# Copy Python Doc
%{__mkdir_p} %{buildroot}%_kde_datadir/doc/python-kde4
%{__cp} -a docs/html/*  %{buildroot}%_kde_datadir/doc/python-kde4/

