%define srcname pykde4

Name:		python-kde4
Summary:	KDE bindings to non-C++ languages
Version:	4.10.2
Release:	1
Epoch:		1
Group:		Development/KDE and Qt
License:	GPLv2
URL:		http://www.kde.org
%define is_beta %(if test `echo %version |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source:		ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/%{srcname}-%{version}.tar.xz
Patch0:		pykde4-4.10.0-respect-sip-flags.patch
BuildRequires:	kdepimlibs4-devel
BuildRequires:	python-sip >= 1:4.13.1
BuildRequires:	python-qt4-devel >= 4.9
BuildRequires:	python-devel
BuildRequires:	automoc4
Provides:	PyKDE4 = %{EVRD}
Provides:	pykde4 = %{EVRD}
Requires:	python-qt4 >= 4.9

%description
The Python bindings for KDE 4.

%files
%{py_platsitedir}/PyQt4/
%{py_platsitedir}/PyKDE4
%{_kde_bindir}/pykdeuic4*
%{_kde_libdir}/kde4/kpythonpluginfactory.so
%dir %{_kde_appsdir}/pykde4
%exclude %{_kde_datadir}/doc/python-kde4

#-----------------------------------------------------------------------------

%package devel
Summary:	PyKDE4 sip files and examples
Group:		Development/KDE and Qt
Conflicts:	python-kde4 < 1:4.5.77-0.svn1198704.2
Requires:	python-kde4 = %{EVRD}
Requires:	python-qt4-devel

%description devel
Python KDE 4 sip files and examples.

%files devel
%{_kde_datadir}/sip/PyKDE4
%{_kde_appsdir}/pykde4/examples

#-----------------------------------------------------------------------------

%package doc
Summary:	PyKDE4 documentation
Group:		Development/KDE and Qt
BuildArch:	noarch

%description doc
Python bindings for KDE 4 documentation.

%files doc
%doc AUTHORS COPYING COPYING.LESSER NEWS README THANKS
%{_kde_datadir}/doc/python-kde4

#------------------------------------------------------------

%prep
%setup -q -n %{srcname}-%{version}
%patch0 -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

# Copy Python Doc
mkdir -p %{buildroot}%{_kde_datadir}/doc/python-kde4
cp -a docs/html/* %{buildroot}%{_kde_datadir}/doc/python-kde4/

%changelog
* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- New version 4.10.0
- Re-diff respect-sip-flags patch (bero)

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.1-1
- New version 4.9.1

* Sat Aug 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.0-1
- New version 4.9.0

* Thu Jul 12 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.97-1
- Update to 4.8.97
- Add pykde4-respect-sip-flags patch from Cooker

* Thu Jun 28 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.95-1
- Update to 4.8.95

* Wed Jun 20 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.90-1
- Update to 4.8.90
- Update BuildRequires (as it now requires python-sip 4.13.1+)

* Fri Jun 08 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.4-1
- update to 4.8.4

* Thu May 10 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.3-1
- update to 4.8.3

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.2-1
- update to 4.8.2

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.1-1
- update to 4.8.1

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.8.0-1
+ Revision: 762417
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.97-1
+ Revision: 758118
- New upstream tarball

* Tue Jan 03 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.95-1
+ Revision: 748827
- Fix file list
- Fix file list
- Fix file list
- Fix file list
- New version

* Wed Dec 14 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.90-1
+ Revision: 740826
- New version

* Tue Nov 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.80-1
+ Revision: 732411
- Add Automoc4 as buildrequires ( to workaround a rpm5/iurt bug)
- New version 4.7.80

* Wed Sep 07 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.41-1
+ Revision: 698633
- imported package python-kde4

